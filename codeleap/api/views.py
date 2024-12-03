from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_datetime')
    serializer_class = PostSerializer

class PostretrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
