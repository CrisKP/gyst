from django.urls import path

from .views import PhotoViewSet

urlpatterns = [
    path('/photos', PhotoViewSet.as_view({"get": "list"})),
    path('/photos/<int:pk>/', PhotoViewSet.as_view({"get": "retrieve"})),
]
