from django.contrib import admin
from django.urls import path, include
from audio_app.apps.audios import views

urlpatterns = [
    path('create_audio/<str:audio_type>/', views.CreateAudioApi.as_view(), name='create_audio'),
    path('delete_audio/<str:audio_type>/<int:audio_id>/', views.DeleteAudioApi.as_view(), name='delete_audio'),
    path('get_audio/<str:audio_type>/', views.GetAudioAPI.as_view(), name='get_audio'),
    path('update_audio/<str:audio_type>/<int:audio_id>/', views.UpdateAudio.as_view(), name='update_audio')
]
