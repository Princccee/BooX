from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # View all books
    path('<int:pk>/', views.book_detail, name='book_detail'),  # Book details
    path('<int:pk>/add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),  # Add to wishlist
    path('search/', views.search_books, name='search_books'),  # Search books
]