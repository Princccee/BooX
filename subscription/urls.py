from django.urls import path
from . import views
from .views import SubscriptionDetailView 

app_name = 'subscription'

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('list/', views.subscription_list, name='subscription_list'),
    path('detail/<int:pk>/', SubscriptionDetailView.as_view(), name='subscription_detail'),
    path('cancel/<int:pk>/', views.cancel_subscription, name='subscription_cancel'),
]