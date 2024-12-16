from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import UserProfile
from books.models import Book


# User Registration
def register(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('book_list')  # Redirect to the book list after registration
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


# User Login
class CustomLoginView(LoginView):
    """
    Handles user login.
    """
    template_name = 'users/login.html'


# User Logout
class CustomLogoutView(LogoutView):
    """
    Handles user logout.
    """
    template_name = 'users/logout.html'


# User Profile
@login_required
def profile(request):
    """
    Allows the user to view and edit their profile.
    """
    # Get or create the user's profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Refresh the profile page after saving
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'users/profile.html', {'form': form, 'profile': profile})


# Wishlist
@login_required
def wishlist(request):
    """
    Displays the books added to the user's wishlist.
    """
    books = request.user.profile.wishlist.all()  # Access wishlist from the Profile model
    return render(request, 'users/wishlist.html', {'books': books})


# Add Book to Wishlist
@login_required
def add_to_wishlist(request, book_id):
    """
    Adds a book to the user's wishlist.
    """
    book = get_object_or_404(Book, id=book_id)
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    profile.wishlist.add(book)
    return redirect('wishlist')


# Remove Book from Wishlist
@login_required
def remove_from_wishlist(request, book_id):
    """
    Removes a book from the user's wishlist.
    """
    book = get_object_or_404(Book, id=book_id)
    profile = UserProfile.objects.get(user=request.user)
    profile.wishlist.remove(book)
    return redirect('wishlist')