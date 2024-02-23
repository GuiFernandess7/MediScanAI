from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

class AuthenticationTest(TestCase):
    def setUp(self):
        self.user_data = {
            'password': 'testpassword',
            'email': 'test@example.com'
        }
        self.user = User.objects.create(**self.user_data)
        self.login_url = '/api/login'
        self.signup_url = '/api/signup'

    def test_login_view(self):
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_registration_view(self):
        new_user_data = {
            'email': 'new_user@example.com',
            'name': "New User Name",
            'password': 'testpassword',
        }
        response = self.client.post(self.signup_url, new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
