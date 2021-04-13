from django.shortcuts import render
from rest_framework.views import APIView
from audio_app.apps.audios.audio_manager import AudioManager
from rest_framework.response import Response
from rest_framework import renderers, status
import json

# Create your views here.

class CreateAudioApi(APIView):

    def post(self, request, audio_type: str):
        data = request.data
        manager = AudioManager(audio_type)
        try:
            resp = manager.create(data)
            if resp['success']:
                return Response(resp, status.HTTP_200_OK)
            return Response(resp, status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            return Response({'error':str(e)}, status.HTTP_400_BAD_REQUEST)
    
    
class DeleteAudioApi(APIView):

    def delete(self, request, audio_type:str, audio_id:int):
        manager = AudioManager(audio_type)
        resp = manager.delete_audio(audio_id)
        if resp['success']:
            return Response(resp, status.HTTP_200_OK)
        else:
            return Response(resp, status.HTTP_422_UNPROCESSABLE_ENTITY)

class GetAudioAPI(APIView):

    def get(self, request, audio_type):
        audio_id = request.query_params.get('audio_id', None)
        manager = AudioManager(audio_type)
        resp = manager.audio_list(audio_id)
        if resp['success']:
            return Response(resp, status.HTTP_200_OK)
        else:
            return Response(resp, status.HTTP_422_UNPROCESSABLE_ENTITY)


class UpdateAudio(APIView):

    def put(self, request, audio_type:str, audio_id:int):
        manager = AudioManager(audio_type, audio_id)
        data = request.data
        try:
            resp = manager.update(data)
            if resp['success']:
                return Response(resp, status.HTTP_200_OK)
            return Response(resp, status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            return Response({'error':str(e)}, status.HTTP_400_BAD_REQUEST)


