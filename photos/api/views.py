from rest_framework import viewsets

from photos.models import Photo
from .serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for viewing uploaded photos.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
