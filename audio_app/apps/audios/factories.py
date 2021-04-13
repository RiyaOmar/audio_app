import factory
from factory import fuzzy
from faker import Faker
from django.utils import timezone
from datetime import date
from datetime import timedelta
from audio_app.apps.audios import models


class AudioTrackFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.AudioTrack
    
    name = factory.Faker('name')
    duration = factory.Faker('pyint')


class SongFactory(AudioTrackFactory):
    class Meta:
        model =  models.Song
    
    artist_name = factory.Faker('text', max_nb_chars=100)


class PodcastFactory(AudioTrackFactory):
    class Meta:
        model = models.Podcast
    
    host = factory.Faker('text', max_nb_chars=100)
    participants = factory.Faker('pylist')


class AudioBook(AudioTrackFactory):
    class Meta:
        model = models.AudioBook
    
    book_name = factory.Faker('name')
    author = factory.Faker('text', max_nb_chars=100)
    narrator = factory.Faker('text', max_nb_chars=100)
