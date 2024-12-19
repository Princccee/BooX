from django.shortcuts import render

# Function to render home page
def home_view(request):
    return render(request, 'core/home.html')