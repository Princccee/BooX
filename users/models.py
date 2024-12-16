from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.user.username


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"


class ReadingProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    progress_percentage = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.progress_percentage}%)"


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page_number = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.book.title} (Page {self.page_number})"