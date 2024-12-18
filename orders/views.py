from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Order, OrderItem
from books.models import Book
from .forms import CheckoutForm
from django.utils.timezone import now


# View Cart
@login_required
def cart_view(request):
    """
    Displays the user's cart with all the books they added.
    """
    cart = request.session.get('cart', {})
    books = []
    total_price = 0

    for book_id, quantity in cart.items():
        book = get_object_or_404(Book, id=book_id)
        books.append({
            'book': book,
            'quantity': quantity,
            'subtotal': book.price * quantity # compute the price of books in cart
        })
        total_price += book.price * quantity

    return render(request, 'orders/cart.html', {'books': books, 'total_price': total_price})


# Add to Cart
@login_required
def add_to_cart(request, book_id):
    """
    Adds a book to the user's cart. Uses session storage for cart data.
    """
    cart = request.session.get('cart', {})
    cart[book_id] = cart.get(book_id, 0) + 1  # Increment the quantity if book already in cart
    request.session['cart'] = cart  # Save cart back to the session
    return redirect('cart_view')


# Remove from Cart
@login_required
def remove_from_cart(request, book_id):
    """
    Removes a book from the user's cart.
    """
    cart = request.session.get('cart', {})
    if book_id in cart:
        del cart[book_id]
    request.session['cart'] = cart  # Save updated cart back to session
    return redirect('cart_view')


# Checkout
@login_required
def checkout(request):
    """
    Displays a checkout form and processes the order on form submission.
    """
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_view')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create Order
            order = Order.objects.create(
                user=request.user,
                shipping_address=form.cleaned_data['shipping_address'],
                order_date=now(),
                status='Pending',
                total_price=0  # Will calculate this in the loop
            )

            total_price = 0
            for book_id, quantity in cart.items():
                book = get_object_or_404(Book, id=book_id)
                subtotal = book.price * quantity
                OrderItem.objects.create(
                    order=order,
                    book=book,
                    quantity=quantity,
                    price=subtotal
                )
                total_price += subtotal

            # Update total price of the order
            order.total_price = total_price
            order.save()

            # Clear the cart
            request.session['cart'] = {}

            return redirect('order_success', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'orders/checkout.html', {'form': form})


# Order Success
@login_required
def order_success(request, order_id):
    """
    Displays a success page after the user places an order.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {'order': order})


# Order History
@login_required
def order_history(request):
    """
    Displays the user's past orders.
    """
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})


# Cancel Order
@login_required
def cancel_order(request, order_id):
    """
    Allows the user to cancel an order if it's still pending.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status == 'Pending':
        order.status = 'Cancelled'
        order.save()
    return redirect('order_history')
