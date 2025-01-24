from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserUpdateForm
from .models import User

# Register a new user
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)  # Accepts uploaded files (e.g., profile_picture)
        if form.is_valid():
            user = form.save(commit=False)  # Don't commit to the DB just yet
            user.is_active = True  # Make sure the user is active
            user.save()
            login(request, user)  # Log in the user automatically after registration
            return redirect('home')  # Redirect to home or another page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


# View and update user profiles
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)  # Load the logged-in user
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the same profile page after updates
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})
