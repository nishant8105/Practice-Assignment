from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from userProfile.filters import UserProfileFilter
from userProfile.models import UserProfile
from userProfile.serializers import UserProfileSerializer
from userProfile.permission import IsProfileOwner


class UserProfileListCreateView(ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_class = UserProfileFilter
    filterset_fields = ['location']
    search_fields = ['user__username', 'bio', 'location']
    ordering_fields = ['id']


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsProfileOwner]
    queryset = UserProfile.objects.all()