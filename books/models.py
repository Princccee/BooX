from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    genre = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title