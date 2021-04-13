from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class AudioTrack(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    uploaded_time = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Song(AudioTrack):
    artist_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Podcast(AudioTrack):
    host = models.CharField(max_length=100)
    participants = ArrayField(models.CharField(max_length=200), null=True, blank=True)

    def __str__(self):
        return self.name


class AudioBook(AudioTrack):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)

    def __str__(self):
        return self.name


