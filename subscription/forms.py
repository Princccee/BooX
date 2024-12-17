from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    PLAN_CHOICES = [
        ('Basic', 'Basic - $5/month'),
        ('Standard', 'Standard - $10/month'),
        ('Premium', 'Premium - $15/month'),
    ]
    
    plan_name = forms.ChoiceField(choices=PLAN_CHOICES, label="Choose a Plan")

    class Meta:
        model = Subscription
        fields = ['plan_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plan_name'].widget.attrs.update({'class': 'form-select'})