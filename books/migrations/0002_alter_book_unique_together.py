# Generated by Django 5.0.6 on 2024-05-24 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authors", "0002_alter_author_name"),
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="book",
            unique_together={("title", "author")},
        ),
    ]
