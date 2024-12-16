# users/forms.py
from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio']  # Add other fields you need

