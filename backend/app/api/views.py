"""
Views for image requests.
"""
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Image
from .serializers import (
    ImageSerializer,
)
from rest_framework import status

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(user=request.user)
        serializer = self.serializer_class(queryset, many=True)
        response = {
            'message': "success",
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, *args, **kwargs):
        image = self.get_object()
        serializer = self.serializer_class(image)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Image, pk=kwargs['pk'])
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
