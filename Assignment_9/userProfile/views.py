from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from userProfile.serializers import PostSerializers
from rest_framework.viewsets import ModelViewSet
from userProfile.models import Post
from rest_framework.permissions import IsAuthenticated
from userProfile.permission import IsPostPossessor
from rest_framework import filters
from userProfile.filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class HelloWorldView(APIView):
    def get(self, request):
        return Response({
            'message' : 'Hello World!'
        })
class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    serializer_class = PostSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PostFilter
    ordering_fields = ['id', ]
    search_fields = ['title', 'content']

    def get_queryset(self):
        return Post.objects.filter(created_by = self.request.user)
