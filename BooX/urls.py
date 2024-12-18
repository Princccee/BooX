"""
URL configuration for BooX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'), name= 'core'), # path to home page
    path('books/', include('books.urls'), name='book'), # path to home app
    path('users/', include('users.urls'), name='users'), # path to users app
    path('orders/', include('orders.urls'), name='orders'), # path to orders app
    path('subscriptions/', include('subscription.urls'), name='subscriptions'), # path to subscription app
    path('reviews/', include('reviews.urls'), name='reviews'),
    path('audiobooks/', include('audiobooks.urls'), name='audiobooks'),
]
