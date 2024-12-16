from django.db import models
from books.models import Book

class Audiobook(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audiobooks/')
    duration = models.DurationField()

    def __str__(self):
        return f"Audiobook: {self.book.title}"