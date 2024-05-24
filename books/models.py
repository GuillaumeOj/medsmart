from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("authors.Author", on_delete=models.CASCADE)

    class Meta:
        unique_together = ["title", "author"]
