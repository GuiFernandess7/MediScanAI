from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status


class APIRequestTest(TestCase):

	def setUp(self):
		self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.login_url = reverse('login')
        self.signup_url = reverse('signup')

    