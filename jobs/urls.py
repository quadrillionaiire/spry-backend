from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),  # List all jobs
    path('<int:job_id>/', views.job_detail, name='job_detail'),  # Job details
]
