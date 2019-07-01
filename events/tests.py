from datetime import datetime

from django.test import TestCase

from .models import Event


class TestEventModel(TestCase):

    def test_event_creation(self):
        Event.objects.create(title="Our first event", date=datetime.utcnow())
        assert Event.objects.all().count() == 1
