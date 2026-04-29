from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Post

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user2 = User.objects.create_user(username='otheruser', password='testpassword')

    def test_hello_world(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'Hello World!')

    # CREATE
    def test_create_post(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/post/', {'title': 'Test Post', 'content': 'Test Content'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().created_by, self.user)

    def test_unauthenticated_post_creation(self):
        response = self.client.post('/post/', {'title': 'Test Post', 'content': 'Test Content'})
        self.assertEqual(response.status_code, 403)

    # READ (LIST & DETAIL)
    def test_list_posts(self):
        Post.objects.create(title='Post 1', content='Content 1', created_by=self.user)
        Post.objects.create(title='Post 2', content='Content 2', created_by=self.user2)
        
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/post/')
        self.assertEqual(response.status_code, 200)
        
        results = response.data['results'] if 'results' in response.data else response.data
        self.assertEqual(len(results), 2)

    def test_retrieve_post(self):
        post = Post.objects.create(title='Post 1', content='Content 1', created_by=self.user)
        
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(f'/post/{post.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Post 1')

    # UPDATE
    def test_update_post(self):
        post = Post.objects.create(title='Old Title', content='Old Content', created_by=self.user)
        
        self.client.force_authenticate(user=self.user)
        response = self.client.put(f'/post/{post.id}/', {'title': 'New Title', 'content': 'New Content'})
        self.assertEqual(response.status_code, 200)
        post.refresh_from_db()
        self.assertEqual(post.title, 'New Title')

    def test_update_post_unauthorized_user(self):
        post = Post.objects.create(title='Old Title', content='Old Content', created_by=self.user)
        
        self.client.force_authenticate(user=self.user2)
        response = self.client.put(f'/post/{post.id}/', {'title': 'New Title', 'content': 'New Content'})
        self.assertEqual(response.status_code, 403)

    # DELETE
    def test_delete_post(self):
        post = Post.objects.create(title='T', content='C', created_by=self.user)
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/post/{post.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Post.objects.count(), 0)

    def test_delete_post_unauthorized_user(self):
        post = Post.objects.create(title='T', content='C', created_by=self.user)
        self.client.force_authenticate(user=self.user2)
        response = self.client.delete(f'/post/{post.id}/')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Post.objects.count(), 1)
