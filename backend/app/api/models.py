"""
Models for Image Analysis.
"""
from django.db import models
from django.contrib.auth import get_user_model

import uuid
import os

def image_file_path(instance, filename):
        """Generate file path for new image"""
        ext = os.path.splitext(filename)[1]
        filename = f'{uuid.uuid4()}{ext}'
        return f'{instance.category.name}-{filename}'

class Image(models.Model):
    """Image model"""

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey('category', on_delete=models.PROTECT, null=False, blank=False, related_name='category_name')
    image = models.ImageField(
                            upload_to=image_file_path,
                            null=False,
                            blank=False
                            )
    results = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name}-{self.created_at}"


class Category(models.Model):
    """Category model"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
