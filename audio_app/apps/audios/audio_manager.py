from audio_app.apps.audios import models
from  audio_app.apps.audios import serializers

class AudioManager(object):
    def __init__(self, audio_type: str, audio_id:int=None):
        self.audio_id = audio_id
        self.audio_type = audio_type
        
    def create(self, data):
        resp = {'success': True}
        if self.audio_type == 'song':
            resp['audio'] = serializers.SongSerializer(self.create_song(data)).data
        elif self.audio_type == 'podcast':
            resp['audio'] = serializers.PodcastSerializer(self.create_podcast(data)).data
        elif self.audio_type == 'book':
            resp['audio'] = serializers. AudioBookSerializer(self.create_book_audio(data)).data
        else:
            resp = {'success': False, "message": "wrong audio type"}
        return resp
    
    def create_song(self, data:dict) -> dict:
        son = models.Song.objects.create(
            name=data.get('name'),
            duration=data.get('duration'),
            artist_name=data.get('artist_name')
        )
        return son

    def create_podcast(self, data) -> dict:
        pod = models.Podcast.objects.create(
            name=data.get('name'),
            duration=data.get('duration'),
            host=data.get('host'),
            participants=data.get('participants')
        )
        return pod
    
    def create_book_audio(self, data:dict) -> dict:
        book = models.AudioBook.objects.create(
            name=data.get('book_name'),
            duration=data.get('duration'),
            book_name=data.get('book_name'),
            author=data.get('author'),
            narrator=data.get('narrator')
        )
        return book

    def delete_audio(self, audio_id:int):
        resp = {}
        if self.audio_type == 'song':
            resp['success'] = self.delete_song(audio_id)
        elif self.audio_type == 'podcast':
            resp['success'] = self.delete_podcast(audio_id)
        elif self.audio_type == 'book':
            resp['success'] = self.delete_book(audio_id)
        else:
            resp = {'success': False, "message": "wrong audio type"}
        return resp
    
    def delete_song(self, audio_id):
        try:
            count, _ = models.Song.objects.filter(id=audio_id).delete()
            return True if count else False
        except Exception as e:
            print(e)
            return False

    
    def delete_podcast(self, audio_id):
        try:
            count, _ = models.Podcast.objects.filter(id=audio_id).delete()
            return True if count else False
        except:
            return False
    
    def delete_book(self, audio_id):
        try:
            count, _ = models.AudioBook.objects.filter(id=audio_id).delete()
            return  True if count else False
        except:
            return False


    def audio_list(self, audio_id:int=None):
        resp = {'success': True}
        many = False if audio_id else True
        if self.audio_type == 'song':
            songs = models.Song.objects.all()
            if audio_id:
                songs = songs.filter(id=audio_id).first()
            resp['audio'] = serializers.SongSerializer(
                songs, many=many
            ).data
        
        elif self.audio_type == 'podcast':
            pod = models.Podcast.objects.all()
            if audio_id:
                pod = pod.filter(id=audio_id).first()
            resp['audio'] = serializers.PodcastSerializer(pod, many=many).data
        elif self.audio_type == 'book':
            book = models.AudioBook.objects.all()
            if audio_id:
                book = book.filter(id=audio_id).first()
            resp['audio'] = serializers.AudioBookSerializer(book, many=many).data
        else:
            resp = {'success': False, "message": "wrong audio type"}
        return resp


    def update(self, data):
        resp = {'success': True}
        if self.audio_type == 'song':
            resp['updated_audio'] = self.update_song(data)
        elif self.audio_type == 'podcast':
            resp['updated_audio'] = self.update_podcast(data)
        elif self.audio_type == 'book':
            resp['updated_audio'] = self.update_book(data)
        else:
            resp = {'success': False, "message": "wrong audio type"}
        return resp

    def update_song(self, data):
        song = models.Song.objects.filter(id=self.audio_id).update(
            name=data.get('name'),
            duration=data.get('duration'),
            artist_name=data.get('artist_name')
        )
        return song
    
    def update_podcast(self, data):
        pod = models.Podcast.objects.filter(id=self.audio_id).update(
            name=data.get('name'),
            duration=data.get('duration'),
            host=data.get('host'),
            participants=data.get('participants')
        )
        return pod

    def update_book(self, data):
        book = models.AudioBook.objects.filter(id=self.audio_id).update(
            name=data.get('book_name'),
            duration=data.get('duration'),
            book_name=data.get('book_name'),
            author=data.get('author'),
            narrator=data.get('narrator')
        )
        return book
