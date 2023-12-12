from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='dan', password='danpassword')

    def test_can_list_posts(self):
        d = User.objects.get(username='dan')
        Post.objects.create(owner=d, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data, len(response.data))

    # def test_logged_in_user_can_create_post(self):
    #     self.client.login(username='d', password='dpassword')
    #     response = self.client.post('/posts/', {'title': 'a title'})
    #     count = Post.objects.count()
    #     self.assertEqual(count, 1)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    # def test_user_not_logged_in_cant_create_post(self):
    #     response = self.client.post('/posts/', {'title': 'a title'})
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    
    
