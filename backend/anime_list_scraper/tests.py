from django.test import TestCase, Client
from django.urls import reverse

class AnimeScrapeTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_scrape_anime_titles(self):
        response = self.client.get(reverse('scrape_anime_titles'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions here to validate the response content
