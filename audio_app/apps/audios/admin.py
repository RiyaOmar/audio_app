from django.contrib import admin
from audio_app.apps.audios import models

# Register your models here.
class AudioTrackAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'uploaded_time', 'modified_at']


admin.site.register(models.AudioTrack, AudioTrackAdmin)
admin.site.register(models.Song)
admin.site.register(models.Podcast)
admin.site.register(models.AudioBook)
