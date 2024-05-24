from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from authors.models import Author
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    author = PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = "__all__"
