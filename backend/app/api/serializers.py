"""
API models serializers.
"""
from rest_framework import serializers
from tempfile import NamedTemporaryFile
import logging
import os

logger = logging.getLogger(__name__)

from api.models import (
    Image,
    Category
)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Image
        fields = ('id', 'category', 'image', 'results',)
        read_only_fields = ('created_at', 'results',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, validated_data):
        image = validated_data['image']
        user = self.context['request'].user
        validated_data['user'] = user
        with NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(image.read())

        try:
            resultados = self.calculate_image_results(temp_file.name)
            validated_data['results'] = resultados
            return super().create(validated_data)
        finally:
            os.remove(temp_file.name)

    def calculate_image_results(self, instance):
        from .preprocessing.brain.preprocess_image import get_image_results
        results = get_image_results(instance, target_size=(150, 150))
        return results
