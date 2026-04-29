from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from userProfile.serializers import PostSerializers
from rest_framework import generics
from userProfile.models import Post
from rest_framework.permissions import IsAuthenticated
from userProfile.permission import IsPostPossessor
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class HelloWorldView(APIView):
    def get(self, request):
        return Response({
            'message' : 'Hello World!'
        })

class PostListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['created_by__username', 'created_on']
    search_fields = ['title', 'content']
    ordering_fields = ['created_on', 'title']

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    queryset = Post.objects.all()
    serializer_class = PostSerializers