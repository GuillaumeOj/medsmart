from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authors.models import Author


class AuthorTests(APITestCase):

    def test_list_authors(self):
        """Ensure we can list all authors."""
        self.author1 = Author.objects.create(name="Author 1")
        self.author2 = Author.objects.create(name="Author 2")
        self.author3 = Author.objects.create(name="Author 3")

        url = reverse("author-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.author1.name)
        self.assertContains(response, self.author2.name)
        self.assertContains(response, self.author3.name)
