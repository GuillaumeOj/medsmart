from rest_framework import mixins, viewsets

from books.models import Book
from books.serializers import BookSerializer


class BookViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
