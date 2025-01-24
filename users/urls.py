from django.urls import path
from .views import register, profile, user_list  # Import your functions/views here
from django.contrib.auth.views import LoginView, LogoutView  # Use Django's built-in authentication views

urlpatterns = [
    path('register/', register, name='register'),  # Registration page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),  # Login page
    path('logout/', LogoutView.as_view(next_page='login', http_method_names=['get', 'post']), name='logout'),  # Allow GET and POST for logout
    path('profile/', profile, name='profile'),  # Profile update page
    path('api/users/', user_list, name='user_list'),  # New API endpoint
]
