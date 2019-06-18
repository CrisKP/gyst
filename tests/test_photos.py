from django.test import TestCase

from photos import views

class TestPhotosViews(TestCase):

    def test_photos_index():
        """Tests that the index page returns a 200 response."""
        response = self.client.get('/')
        assert response.status_code == 200
