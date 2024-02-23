"""
Tests for user models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from django.urls import reverse
from django.test import Client


class ModelTests(TestCase):
    """Test user creation model."""

    def test_create_user_with_email_successfull(self):
        """Test creating a user with an email successfull."""
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_superuser_with_email_successfull(self):
        """Test creating a super user with an email successfull."""
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


class AdminSiteTests(TestCase):
    """Test for Django admin."""

    def setUp(self):
        """Create user and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
        )

    def test_users_list(self):
        """Test that users are listed on page."""
        url = reverse('admin:users_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test the edit user page works."""
        url = reverse('admin:users_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test the create user page works."""
        url = reverse('admin:users_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)