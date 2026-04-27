from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from helloworld.serializers import PostSerializers
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
# Create your views here.

class HelloWorld(APIView):
    def get(self, response):
        return Response({'message' : 'Hello world'})
    
class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers