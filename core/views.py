from django.shortcuts import render
from rest_framework import generics,permissions,status
from rest_framework.response import Response

from core.serializers import PostSerializer
from .models import Post
# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

