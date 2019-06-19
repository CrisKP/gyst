from django.test import TestCase, Client

from photos import views

class TestPhotosViews(TestCase):


    c = Client()

    def test_photos_index(self):
        import pdb; pdb.set_trace()
        """Tests that the index page returns a 200 response."""
        response = self.c.get('/')
        assert response.status_code == 200

    def test_photos_gallery(self):
        response = self.c.get('/photos/gallery')
        assert response.status_code == 200
