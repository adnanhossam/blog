from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import Client , TestCase
from django.urls import reverse
from .views import Post

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username= 'testuser',
            email='testemail',
            password='secret',
        )

        self.post = Post.objects.create(
            title = 'a good title',
            body = 'nice body content',
            author = self.user,
        )

        def test_string_representation(self):
            post=Post(title='a sample title')
            self.assertEqual(str(post), post.title)

        def test_post_content(self):
            response = self.client.get('/post/1')
            no_response = self.client.get('/post/100000')
            self.assertEqual(response.status_code,200)
            self.assertEqual(no_response.status_code,404)
            self.assertContains(response,'a good title')
            self.assertTemplateUsed(response, 'post_detail.html')
