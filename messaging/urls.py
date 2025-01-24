from django.urls import path
from . import views

urlpatterns = [
    path('', views.message_list, name='message_list'),  # List all messages
    path('<int:message_id>/', views.message_detail, name='message_detail'),  # Message details
]
