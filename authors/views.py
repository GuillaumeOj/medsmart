from rest_framework import mixins, viewsets

from authors.models import Author
from authors.serializers import AuthorSerializer


class AuthorViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
