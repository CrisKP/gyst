from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer


class EventsView(viewsets.ModelViewSet):
    """
    A simple viewset for viewing and editing
    events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
