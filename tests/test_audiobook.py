import json
import io,os
from werkzeug.datastructures import FileStorage
from tests.BaseCase import BaseCase
import random
import datetime
from models.audiobook import AudibookModel


class TestUploadAudiBook(BaseCase):
    def test_successful_audiobook_upload(self):
        
        _id = random.randint(1,1000)
        my_audio = os.path.join("tests/test_files/test.wav")
        
        my_file = FileStorage(
            stream=open(my_audio, "rb"),
            filename="test.wav"),
        user_payload={'duration': '36',
        'upload_time': '2021-06-29T08:15:27',
        'audioFileType': 'audiobook',
        'audioFileID': _id,
        'name': 'pankha',
        'participants': 'jhh',
        'author': 'amit',
        'narrator': 'amit' }
        # user_payload['file'] = (io.BytesIO(b"abcdef"), 'test_files\a.jpg')
        user_payload['file'] = my_file
        headers = {}
    
        response = self.app.post('/audio', headers=headers, data=user_payload)
        print(response.json)
        self.assertEqual(201, response.status_code)

    def test_successful_audiobook_put(self):
        
        _id = random.randint(1,1000)
        my_audio = os.path.join("tests/test_files/test.wav")
        
        my_file = FileStorage(
            stream=open(my_audio, "rb"),
            filename="test.wav"),
        user_payload={'duration': '36',
        'upload_time': '2021-06-29T08:15:27',
        'audioFileType': 'audiobook',
        'audioFileID': _id,
        'name': 'pankha',
        'participants': 'jhh',
        'author': 'amit',
        'narrator': 'amit' }
        # user_payload['file'] = (io.BytesIO(b"abcdef"), 'test_files\a.jpg')
        user_payload['file'] = my_file
        headers = {}
    
        response = self.app.put('/audio', headers=headers, data=user_payload)
        print(response.json)
        self.assertEqual(200, response.status_code)

    def test_upload_invalid_id(self):
        my_audio = os.path.join("tests/test_files/test.wav")
        
        my_file = FileStorage(
            stream=open(my_audio, "rb"),
            filename="test.wav"),
        user_payload={'duration': '36',
        'upload_time': '2021-06-29T08:15:27',
        'audioFileType': 'audiobook',
        'audioFileID': 829,
        'name': 'pankha',
        'host': 'mina',
        'participants': 'jhh',
        'author': 'amit',
        'narrator': 'amit' }
        # user_payload['file'] = (io.BytesIO(b"abcdef"), 'test_files\a.jpg')
        user_payload['file'] = my_file
        headers = {}
    
        response = self.app.post('/audio', headers=headers, data=user_payload)
        print(response.json)
        self.assertEqual(400, response.status_code)
        self.assertEqual("Audio with given audioFileID already exists", response.json['message'])

    def test_upload_str_id(self):
        my_audio = os.path.join("tests/test_files/test.wav")
        
        my_file = FileStorage(
            stream=open(my_audio, "rb"),
            filename="test.wav"),
        user_payload={'duration': '36',
        'upload_time': '2021-06-29T08:15:27',
        'audioFileType': 'audiobook',
        'audioFileID': 'asa',
        'name': 'pankha',
        'host': 'mina',
        'participants': 'jhh',
        'author': 'amit',
        'narrator': 'amit' }
        # user_payload['file'] = (io.BytesIO(b"abcdef"), 'test_files\a.jpg')
        user_payload['file'] = my_file
        headers = {}
    
        response = self.app.post('/audio', headers=headers, data=user_payload)
        print(response.json)
        
    def test_upload_numeric_name(self):
        _id = random.randint(1,1000)
        my_audio = os.path.join("tests/test_files/test.wav")
        
        my_file = FileStorage(
            stream=open(my_audio, "rb"),
            filename="test.wav"),
        user_payload={'duration': '36',
        'upload_time': '2021-06-29T08:15:27',
        'audioFileType': 'audiobook',
        'audioFileID': _id,
        'name': 123,
        'host': 'mina',
        'participants': 'jhh',
        'author': 'amit',
        'narrator': 'amit' }
        # user_payload['file'] = (io.BytesIO(b"abcdef"), 'test_files\a.jpg')
        user_payload['file'] = my_file
        headers = {}
    
        response = self.app.post('/audio', headers=headers, data=user_payload)
        print(response.json)
        self.assertEqual(400, response.status_code)

    def test_upload_morethanhundred_name(self):
        _id = random.randint(1,1000)
        my_audio = os.path.join("tests/test_files/test.wav")
        
        my_file = FileStorage(
            stream=open(my_audio, "rb"),
            filename="test.wav"),
        user_payload={'duration': '36',
        'upload_time': '2021-06-29T08:15:27',
        'audioFileType': 'audiobook',
        'audioFileID': _id,
        'name': 'sdsdsdsdsdsdsadsadsdsdsdasdsadasdasdasdsadsdsdsadasdasdsdsdsadsadsdsdsdsdsdsdsddsdsfdfdfdfdfdfdfdfdfdfdf',
        'host': 'mina',
        'participants': 'jhh',
        'author': 'amit',
        'narrator': 'amit' }
        # user_payload['file'] = (io.BytesIO(b"abcdef"), 'test_files\a.jpg')
        user_payload['file'] = my_file
        headers = {}
    
        response = self.app.post('/audio', headers=headers, data=user_payload)
        print(response.json)
        self.assertEqual(400, response.status_code)

    def test_upload_nonnumeric_duration(self):
        
        _id = random.randint(1,1000)
        my_audio = os.path.join("tests/test_files/test.wav")
        
        my_file = FileStorage(
            stream=open(my_audio, "rb"),
            filename="test.wav"),
        user_payload={'duration': 'sdax',
        'upload_time': '2021-06-29T08:15:27',
        'audioFileType': 'audiobook',
        'audioFileID': _id,
        'name': 'pankha',
        'host': 'mina',
        'participants': 'jhh',
        'author': 'amit',
        'narrator': 'amit' }
        # user_payload['file'] = (io.BytesIO(b"abcdef"), 'test_files\a.jpg')
        user_payload['file'] = my_file
        headers = {}
    
        response = self.app.post('/audio', headers=headers, data=user_payload)
        print(response.json)
        self.assertEqual(400, response.status_code)

    def test_upload_negative_duration(self):
        
        _id = random.randint(1,1000)
        my_audio = os.path.join("tests/test_files/test.wav")
        
        my_file = FileStorage(
            stream=open(my_audio, "rb"),
            filename="test.wav"),
        user_payload={'duration': '-1',
        'upload_time': '2021-06-29T08:15:27',
        'audioFileType': 'audiobook',
        'audioFileID': _id,
        'name': 'pankha',
        'host': 'mina',
        'participants': 'jhh',
        'author': 'amit',
        'narrator': 'amit' }
        # user_payload['file'] = (io.BytesIO(b"abcdef"), 'test_files\a.jpg')
        user_payload['file'] = my_file
        headers = {}
    
        response = self.app.post('/audio', headers=headers, data=user_payload)
        print(response.json)
        self.assertEqual(400, response.status_code)

    def test_upload_past_UploadDate(self):
        
        _id = random.randint(1,1000)
        my_audio = os.path.join("tests/test_files/test.wav")
        
        my_file = FileStorage(
            stream=open(my_audio, "rb"),
            filename="test.wav"),
        user_payload={'duration': '36',
        'upload_time': '2019-06-29T08:15:27',
        'audioFileType': 'audiobook',
        'audioFileID': _id,
        'name': 'pankha',
        'host': 'dsd',
        'participants': 'a,b',
        'author': 'amit',
        'narrator': 'amit' }
        # user_payload['file'] = (io.BytesIO(b"abcdef"), 'test_files\a.jpg')
        user_payload['file'] = my_file
        headers = {}
    
        response = self.app.post('/audio', headers=headers, data=user_payload)
        print(response.json)
        self.assertEqual(400, response.status_code)

    def test_upload_invalid_narrator(self):
        
        _id = random.randint(1,1000)
        my_audio = os.path.join("tests/test_files/test.wav")
        
        my_file = FileStorage(
            stream=open(my_audio, "rb"),
            filename="test.wav"),
        user_payload={'duration': '36',
        'upload_time': '2019-06-29T08:15:27',
        'audioFileType': 'audiobook',
        'audioFileID': _id,
        'name': 'pankha',
        'host': 'dsd',
        'participants': 'a,b',
        'author': 'amit',
        'narrator': '' }
        # user_payload['file'] = (io.BytesIO(b"abcdef"), 'test_files\a.jpg')
        user_payload['file'] = my_file
        headers = {}
    
        response = self.app.post('/audio', headers=headers, data=user_payload)
        print(response.json)
        self.assertEqual(400, response.status_code)

    def test_successful_audiobook_get(self):
        
        _id = random.randint(1,1000)
        my_audio = os.path.join("tests/test_files/test.wav")
        
        my_file = FileStorage(
            stream=open(my_audio, "rb"),
            filename="test.wav"),
        user_payload={'duration': '36',
        'upload_time': '2021-06-29T08:15:27',
        'audioFileType': 'audiobook',
        'audioFileID': _id,
        'name': 'pankha',
        'participants': 'jhh',
        'author': 'amit',
        'narrator': 'amit' }
        # user_payload['file'] = (io.BytesIO(b"abcdef"), 'test_files\a.jpg')
        user_payload['file'] = my_file
        headers = {}
    
        response = self.app.post('/audio', headers=headers, data=user_payload)
        print(response.json)
        self.assertEqual(201, response.status_code)
        
        response = self.app.get('/audio/audiobook/{}'.format(_id), headers={}, data={})
        self.assertEqual(200, response.status_code)

    def test_unsuccessful_audiobook_get(self):
        _id = 123434343
        response = self.app.get('/audio/audiobook/{}'.format(_id), headers={}, data={})
        self.assertEqual(404, response.status_code)

    def test_unsuccessful_audiobook_getall(self):
        response = self.app.get('/audio/audiobook', headers={}, data={})
        self.assertEqual(200, response.status_code)

    def test_successful_audiobook_delete(self):
        
        _id = random.randint(1,1000)
        my_audio = os.path.join("tests/test_files/test.wav")
        
        my_file = FileStorage(
            stream=open(my_audio, "rb"),
            filename="test.wav"),
        user_payload={'duration': '36',
        'upload_time': '2021-06-29T08:15:27',
        'audioFileType': 'audiobook',
        'audioFileID': _id,
        'name': 'pankha',
        'participants': 'jhh',
        'author': 'amit',
        'narrator': 'amit' }
        # user_payload['file'] = (io.BytesIO(b"abcdef"), 'test_files\a.jpg')
        user_payload['file'] = my_file
        headers = {}
    
        response = self.app.post('/audio', headers=headers, data=user_payload)
        print(response.json)
        self.assertEqual(201, response.status_code)
        
        response = self.app.delete('/audio/audiobook/{}'.format(_id), headers={}, data={})
        self.assertEqual(200, response.status_code)

    def test_unsuccessful_audiobook_delete(self):
        _id = 878787787
        response = self.app.delete('/audio/audiobook/{}'.format(_id), headers={}, data={})
        self.assertEqual(404, response.status_code)

   