from db import db
import os
from resources.serializers import fileparser
from flask import current_app as app,send_file
import shutil
from resources.serializers import audiobookparser
import zipfile

class AudibookModel(db.Model):
    __tablename__ = 'audiobook'

    audio_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    narrator = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime)
    file_path = db.Column(db.String(120))
    input_parser = audiobookparser

    def __init__(self,audio_id,name,author,narrator, duration, upload_time,file_path):
        self.audio_id = audio_id
        self.name = name
        self.author = author
        self.narrator = narrator
        self.duration = duration
        self.upload_time = upload_time
        self.file_path = file_path

    def json(self):
        return {'audio_id': self.audio_id,
                'name': self.name, 
                'author':self.author,
                'narrator':self.narrator,
                'duration': self.duration,
                'upload_time':str(self.upload_time),
                'file_path':self.file_path}

    @classmethod
    def find_by_name(cls, audio_id):
        return cls.query.filter_by(audio_id=audio_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def save_update_file(cls,audio_id):
        file = fileparser.parse_args()['file']
        target = "/".join([app.config['AUDIOFILES_UPLOAD_FOLDER'],str(audio_id)])

        if not os.path.isdir(target):
            os.makedirs(target)
            # print("{} directory does not exist".format(target))
        else:
            # print("{} directory exist".format(target))
            shutil.rmtree(target,ignore_errors=True)
            os.makedirs(target)
        destination = "/".join([target,file.filename])
        file.save(destination)
        return destination

    @classmethod
    def delete_file(cls,audio_id):
        shutil.rmtree("/".join([app.config['AUDIOFILES_UPLOAD_FOLDER'],str(audio_id)]),ignore_errors=True)

    @classmethod
    def download_all(cls):
        target_dir = app.config['AUDIOFILES_UPLOAD_FOLDER']
        foldername = 'AudioFiles/archive/audiobook.zip'
        shutil.rmtree(str(foldername),ignore_errors=True)
        zipobj = zipfile.ZipFile(foldername, 'w', zipfile.ZIP_DEFLATED)
        rootlen = len(target_dir) + 1
        for base, dirs, files in os.walk(target_dir):
            for file in files:
                fn = os.path.join(base, file)
                zipobj.write(fn, fn[rootlen:])
        return foldername


