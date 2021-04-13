from rest_framework.test import APITestCase
from audio_app.apps.audios import factories
from audio_app.apps.audios import models

class CreateAudioApiView(APITestCase):
    """
    test caes for create API
    """
    databases = '__all__'
    URL = '/audios/create_audio'
    def test_create_api_with_missing_data_for_song(self):
        data = {
            "name": "Song3",
            "artist_name": "Jacob1"
        }
        response = self.client.post(f'{self.URL}/song/', data=data, format='json')
        self.assertEqual(response.status_code, 400)
    
    def test_create_api_for_song(self):
        data = {
            "name": "song",
            "duration": 5,
            "artist_name": "jaco"
        }
        response = self.client.post(f'{self.URL}/song/', data=data, format='json')
        self.assertEqual(response.status_code, 200)

    
    def test_create_api_for_wrong_audio_type(self):

        data = {}
        response = self.client.post(f'{self.URL}/playlist/', data=data, format='json')
        self.assertEqual(response.status_code, 422)

    def test_create_api_for_podcast_missing_data(self):
        data = {
                "name": "pod1",
                "host": "host"
            }
        response = self.client.post(f'{self.URL}/podcast/', data=data, format='json')
        self.assertEqual(response.status_code, 400)
    
    def test_create_api_for_podcast_with_partcipants(self):
        data = {
            "name": "pod1",
            "host": "host",
            "duration": 4,
            "participants": ["P1", "p2", "p3"]
        }
        response = self.client.post(f'{self.URL}/podcast/', data=data, format='json')
        self.assertEqual(response.status_code, 200)
    
    def test_create_api_for_podcast_without_participants(self):
        data = {
            "name": "pod1",
            "host": "host",
            "duration": 6
        }
        response = self.client.post(f'{self.URL}/podcast/', data=data, format='json')
        self.assertEqual(response.status_code, 200)
    
    def test_create_api_for_books(self):
        data = {
            "book_name": "book1",
            "author": "author1",
            "narrator": "narrator1",
            "duration": 3
        }
        response = self.client.post(f'{self.URL}/book/', data=data, format='json')
        self.assertEqual(response.status_code, 200)
    
    def test_create_api_for_missing_data_in_book(self):
        data = {
            "book_name": "book1",
            "author": "author1",
            "narrator": "narrator1",
        }
        response = self.client.post(f'{self.URL}/book/', data=data, format='json')
        self.assertEqual(response.status_code, 400)
        

class DeleteAudioApi(APITestCase):

    URL = '/audios/delete_audio'
    def setUp(self):
        self.song1 = factories.SongFactory()
        self.book1 = factories.AudioBook()
        self.podcast = factories.PodcastFactory()
    
    def test_delete_api_for_song(self):
        response =  self.client.delete(f'{self.URL}/song/{self.song1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_delete_api_for_song_with_wrong_id(self):
        response = self.client.delete(f'{self.URL}/song/0/')
        self.assertEqual(response.status_code, 422)
    
    def test_delete_api_with_wrong_audio_type(self):
        response =  self.client.delete(f'{self.URL}/songa/{self.song1.id}/')
        self.assertEqual(response.status_code, 422)
    
    def test_delete_api_for_book(self):
        response =  self.client.delete(f'{self.URL}/book/{self.book1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_delete_api_for_song_with_wrong_id(self):
        response = self.client.delete(f'{self.URL}/book/0/')
        self.assertEqual(response.status_code, 422)
    
    def test_delete_api_for_song(self):
        response =  self.client.delete(f'{self.URL}/podcast/{self.podcast.id}/')
        self.assertEqual(response.status_code, 200)

    def test_delete_api_for_song_with_wrong_id(self):
        response = self.client.delete(f'{self.URL}/podcast/0/')
        self.assertEqual(response.status_code, 422)
    

class GetAudioAPI(APITestCase):
    URL = '/audios/get_audio'
    def setUp(self):
        self.song1 = factories.SongFactory()
        self.book1 = factories.AudioBook()
        self.podcast = factories.PodcastFactory()
        for i in range(0,10):
            factories.SongFactory()
            factories.PodcastFactory()
            factories.AudioBook()
    
    def test_get_api_for_song_for_with_song_id(self):
        response = self.client.get(f'{self.URL}/song/?audio_id={self.song1.id}')
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(response['audio']['id'], self.song1.id)
        self.assertEqual(response['audio']['name'], self.song1.name)

    def test_get_api_for_song_without_song_id(self):
        response = self.client.get(f'{self.URL}/song/')
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response['audio']), 11)
    
    def test_get_api_for_wrong_audio_type(self):
        response = self.client.get(f'{self.URL}/song1/?audio_id={self.song1.id}')
        self.assertEqual(response.status_code, 422)
    
    def test_get_api_for_song_for_with_podcast_id(self):
        response = self.client.get(f'{self.URL}/podcast/?audio_id={self.podcast.id}')
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(response['audio']['id'], self.podcast.id)
        self.assertEqual(response['audio']['name'], self.podcast.name)

    def test_get_api_for_song_without_podcast_id(self):
        response = self.client.get(f'{self.URL}/podcast/')
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response['audio']), 11)
    
    def test_get_api_for_song_for_with_book_id(self):
        response = self.client.get(f'{self.URL}/book/?audio_id={self.book1.id}')
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(response['audio']['id'], self.book1.id)
        self.assertEqual(response['audio']['name'], self.book1.name)

    def test_get_api_for_song_without_book_id(self):
        response = self.client.get(f'{self.URL}/book/')
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response['audio']), 11)


class UpdateAudioAPI(APITestCase):
    URL = '/audios/update_audio'
    
    def setUp(self):
        self.song1 = factories.SongFactory(name="New Song", duration=7, artist_name="Sin")
        self.book1 = factories.AudioBook(name="Pod Data", duration=3)
        self.podcast = factories.PodcastFactory(name="Amis")
    
    def test_update_api_for_song(self):
        data = {
            "name": "song",
            "duration": 5,
            "artist_name": "jaco"
        }
        response = self.client.put(f'{self.URL}/song/{self.song1.id}/', data=data, format='json')
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(response['updated_audio'], 1)
        db_data = models.Song.objects.filter(id=self.song1.id).first()
        self.assertEqual(db_data.name, "song")

    
    def test_update_api_for_song_without_id(self):
        data = {
            "name": "song",
            "duration": 5,
            "artist_name": "jaco"
        }
        response = self.client.put(f'{self.URL}/song/', data=data, format='json')
        self.assertEqual(response.status_code, 404)
    
    def test_update_api_for_podcast(self):
        data = {
            "name": "pod1",
            "host": "host",
            "duration": 4,
            "participants": ["P1", "p2", "p3"]
        }
        response = self.client.put(f'{self.URL}/podcast/{self.podcast.id}/', data=data, format='json')
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(response['updated_audio'], 1)
        db_data = models.Podcast.objects.filter(id=self.podcast.id).first()
        self.assertEqual(db_data.name, "pod1")

    
    def test_update_api_for_podcast_without_id(self):
        data = {
            "name": "pod1",
            "host": "host",
            "duration": 4,
            "participants": ["P1", "p2", "p3"]
        }
        response = self.client.put(f'{self.URL}/podcast/', data=data, format='json')
        self.assertEqual(response.status_code, 404)

    def test_update_api_for_bookaudio(self):
        data = {
            "book_name": "book1",
            "author": "author1",
            "narrator": "narrator1",
            "duration": 3
        }
        response = self.client.put(f'{self.URL}/book/{self.book1.id}/', data=data, format='json')
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(response['updated_audio'], 1)
        db_data = models.AudioBook.objects.filter(id=self.book1.id).first()
        self.assertEqual(db_data.name, "book1")

    
    def test_update_api_for_book_without_id(self):
        data = {
            "book_name": "book1",
            "author": "author1",
            "narrator": "narrator1",
            "duration": 3
        }
        response = self.client.put(f'{self.URL}/book/', data=data, format='json')
        self.assertEqual(response.status_code, 404)