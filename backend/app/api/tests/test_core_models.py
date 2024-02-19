"""
Test API models.
"""

from django.test import TestCase
from unittest.mock import patch

from api.models import (
    Category,
    Image,
    image_file_path
)

class ModelTests(TestCase):
    """Test main models."""

    @patch('api.models.uuid.uuid4')
    def test_image_file_name_uuid(self, mock_uuid):
        """Test generating image path"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        category = Category.objects.create(name='test-category')
        image = Image(category=category)
        file_path = image_file_path(image, 'example.jpg')

        self.assertEqual(file_path, f'{category.name}-{uuid}.jpg')
