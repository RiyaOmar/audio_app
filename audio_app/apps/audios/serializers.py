from rest_framework import serializers
from audio_app.apps.audios import models

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AudioTrack
        fields = '__all__'
    
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model =  models.Song
        fields = '__all__'

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Podcast
        fields = '__all__'

class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AudioBook
        fields = '__all__'