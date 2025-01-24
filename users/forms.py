from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form with additional fields like bio, profile_picture, and social_links.
    """
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Tell us about yourself...', 'rows': 3}),
        help_text="Optional: Write a short bio about yourself."
    )
    profile_picture = forms.ImageField(
        required=False,
        help_text="Optional: Upload a profile picture."
    )
    social_links = forms.URLField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g., https://yourwebsite.com'}),
        help_text="Optional: Add a link to your social media or personal website."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio', 'profile_picture', 'social_links']


class UserUpdateForm(forms.ModelForm):
    """
    Form to allow users to update their profile.
    """
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Update your bio...', 'rows': 3}),
        help_text="Optional: Update your bio here."
    )
    profile_picture = forms.ImageField(
        required=False,
        help_text="Optional: Upload a new profile picture."
    )
    social_links = forms.URLField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g., https://yourwebsite.com'}),
        help_text="Optional: Update your social media or personal website."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'profile_picture', 'social_links']
