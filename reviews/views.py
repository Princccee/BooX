from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Review

# View to display a list of reviews
def review_list(request):
    reviews = Review.objects.all()  # Get all reviews from the database
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

# View to display the details of a single review
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)  # Get a review by primary key or return 404 if not found
    return render(request, 'reviews/review_detail.html', {'review': review})