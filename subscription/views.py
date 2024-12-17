from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Subscription
from .forms import SubscriptionForm
from django.utils import timezone

# View to display all subscriptions
@login_required
def subscription_list(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    return render(request, 'subscriptions/subscription_list.html', {'subscriptions': subscriptions})

# View to create a new subscription
# @login_required
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.user = request.user
            subscription.start_date = timezone.now()
            subscription.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionForm()
    return render(request, 'subscriptions/subscribe.html', {'form': form})

# View to cancel a subscription
@login_required
def cancel_subscription(request, subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id, user=request.user)
    if request.method == 'POST':
        subscription.status = 'Cancelled'
        subscription.end_date = timezone.now()
        subscription.save()
        return redirect('subscription_list')
    return render(request, 'subscriptions/cancel_subscription.html', {'subscription': subscription})

# Class-Based View for Subscription Details
class SubscriptionDetailView(View):
    def get(self, request, subscription_id):
        subscription = get_object_or_404(Subscription, id=subscription_id, user=request.user)
        return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})

# API Endpoint to check subscription status
@login_required
def subscription_status(request):
    active_subscription = Subscription.objects.filter(user=request.user, status='Active').exists()
    return JsonResponse({'has_active_subscription': active_subscription})