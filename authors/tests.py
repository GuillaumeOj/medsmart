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

    def test_create_author(self):
        """Ensure we can create a new author."""
        url = reverse("author-list")

        # The author's name is missing
        data = {}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Author.objects.count(), 0)
        self.assertIn("name", response.data.keys())

        # The author's name is empty
        data = {"name": ""}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Author.objects.count(), 0)
        self.assertIn("name", response.data.keys())

        # The author's name is provided
        data = {"name": "Author 1"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.get().name, "Author 1")

        # The author's name already exists
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Author.objects.count(), 1)
        self.assertIn("name", response.data.keys())
