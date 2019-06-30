from django.db import models


class Event(models.Model):
    """
    A model representing an individual event.
    Each event will have it's own Event object; Event
    objects should not be reused.
    """
    title = models.CharField(max_length=200)
    date = models.DateTimeField(blank=True)
    location = models.CharField(max_length=200, blank=True)
