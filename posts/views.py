from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Like, Comment
from .serializers import PostSerializer, LikeSerializer, CommentSerializer

class PostListCreateView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Assign the logged-in user to the post
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
