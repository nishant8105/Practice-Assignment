import django_filters
from userProfile.models import Post
from django import forms

class PostFilter(django_filters.FilterSet):
    created_on = django_filters.DateFilter(
        widget = forms.DateInput(attrs={'type': 'date'}),
        field_name='created_on',
        lookup_expr='date__exact'
    )

    class Meta:
        model = Post
        fields = ['created_on']