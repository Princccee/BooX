from django.shortcuts import get_object_or_404, render
from .models import Book  #Impor the book model

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def add_to_wishlist(request, pk):
    book = get_object_or_404(Book, pk=pk)
    request.user.profile.wishlist.add(book)  # Assuming a many-to-many field `wishlist` in a User Profile model
    return HttpResponseRedirect(reverse('book_detail', args=[pk]))

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(authors__name__icontains=query) | Book.objects.filter(genre__name__icontains=query)
    return render(request, 'books/book_list.html', {'books': books, 'query': query})

