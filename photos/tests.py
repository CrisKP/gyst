from tests.utils import SeleniumTestCase

# from .models import Photo


class TestPhotosUrls(SeleniumTestCase):

    # def setUp(self):
    #     Photo.objects.create(file="tests/test_data/test_1.jpg", caption="First Photo")

    # def tearDown(self):
    #     Photo.objects.all().delete()

    # We need google cloud auth settings to work on tests

    def test_photos_index(self):
        self.browser.get('http://127.0.0.1:8000/photos')
        text = self.browser.find_element_by_tag_name('body').text
        assert "This is the photos main page" in text

    def test_photos_gallery(self):
        self.browser.get('http://127.0.0.1:8000/photos/gallery')
        text = self.browser.find_element_by_tag_name('body').text
        assert "Photo Gallery" in text

    def test_photos_upload(self):
        self.browser.get('http://127.0.0.1:8000/photos/upload')
        text = self.browser.find_element_by_tag_name('body').text
        assert "File:" in text
        assert "Caption" in text
        assert "Return to the photos main page" in text
