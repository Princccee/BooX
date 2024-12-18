from django.urls import path
from .views import AudiobookListView, AudiobookDetailView, AudiobookCreateView

app_name = 'audiobooks'

urlpatterns = [
    path('', AudiobookListView.as_view(), name='list'),  # List of audiobooks
    path('<int:pk>/', AudiobookDetailView.as_view(), name='detail'),  # Details of a single audiobook
    path('add/', AudiobookCreateView.as_view(), name='add'),  # Add a new audiobook
]