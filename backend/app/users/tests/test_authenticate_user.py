from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse

class AuthenticationTest(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.login_url = reverse('login')
        self.signup_url = reverse('signup')

    def test_login_view(self):
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tokens', response.data.keys())

    def test_registration_view(self):
        new_user_data = {
            'email': 'new_user@example.com',
            'name': "New User Name",
            'password': 'testpassword',
        }
        response = self.client.post(self.signup_url, new_user_data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)