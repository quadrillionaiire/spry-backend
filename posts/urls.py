from django.urls import path
from .views import PostListCreateView, PostDetailView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post_list'),
    path('<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
]
