from django.shortcuts import render

# Create your views here.

# Function to render home page
def home_view(request):
    return render(request, 'core/home.html') 