from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authors.models import Author
from books.models import Book


class BookTests(APITestCase):

    def setUp(self):
        super().setUp()
        self.author1 = Author.objects.create(name="Author 1")
        self.author2 = Author.objects.create(name="Author 2")

    def test_list_books(self):
        """Ensure we can list all books."""
        self.book1 = Book.objects.create(title="Book 1", author=self.author1)
        self.book2 = Book.objects.create(title="Book 2", author=self.author1)
        self.book3 = Book.objects.create(title="Book 3", author=self.author2)

        url = reverse("book-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book2.title)
        self.assertContains(response, self.book3.title)

    def test_create_book(self):
        """Ensure we can create a new book."""
        url = reverse("book-list")

        # The book's title is missing
        data = {"author": self.author1.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data.keys())
        self.assertEqual(Book.objects.count(), 0)

        # The book's author is missing
        data = {"title": "foo"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("author", response.data.keys())
        self.assertEqual(Book.objects.count(), 0)

        # The book's author does not exist
        data = {"title": "foo", "author": 999}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("author", response.data.keys())
        self.assertEqual(Book.objects.count(), 0)

        # The book's is created
        data = {"title": "foo", "author": self.author1.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        book = Book.objects.get()
        self.assertEqual(book.title, "foo")
        self.assertEqual(book.author_id, self.author1.id)

        # The book's title already exists for this author
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.count(), 1)
        error = response.data["non_field_errors"][0]
        self.assertEqual(str(error), "The fields title, author must make a unique set.")
