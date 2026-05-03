from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from userProfile.models import UserProfile


class UserProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def test_create_profile(self):
        response = self.client.post('/api/users/', {
            'bio': 'Test bio',
            'location': 'India'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_profile(self):
        profile = UserProfile.objects.create(user=self.user)
        response = self.client.get(f'/api/users/{profile.pk}/')
        self.assertEqual(response.status_code, 200)