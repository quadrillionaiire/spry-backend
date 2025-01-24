from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),  # List all events
    path('<int:event_id>/', views.event_detail, name='event_detail'),  # Event details
]
