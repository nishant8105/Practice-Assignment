import django_filters
from userProfile.models import UserProfile


class UserProfileFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(lookup_expr='icontains')
    username = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')

    class Meta:
        model = UserProfile
        fields = ['location', 'username']