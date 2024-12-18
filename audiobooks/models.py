from django.db import models
from django.utils.timezone import now
from datetime import timedelta

class Audiobook(models.Model):
    title = models.CharField(max_length=200, default="Untitled Audiobook")  # Default title for missing data
    author = models.CharField(max_length=100, default="Unknown Author")  # Default author
    narrator = models.CharField(max_length=100, default="Unknown Narrator")  # Default narrator
    duration = models.DurationField(default=timedelta(hours=1))  # Default duration of 1 hour
    description = models.TextField(default="No description available.")  # Default description
    uploaded_at = models.DateTimeField(default=now)  # Default to the current date and time

    def __str__(self):
        return self.title