from flask_restful import Resource, reqparse
from flask import current_app as app,send_file
from models.song import SongModel
from models.podcast import PodCastModel
from models.audiobook import AudibookModel
from .serializers import songparser,podcastparser,audiobookparser
from resources.errors import errors
import os

class Store(Resource):
    @classmethod
    def get_fileType(cls,audioFileType):
        if audioFileType == "song":
            mod = SongModel
        elif audioFileType == "podcast":
            mod = PodCastModel
        elif audioFileType == "audiobook":
            mod = AudibookModel
        return mod

    def get(self, audioFileType,audioFileID=None):
        mod = Store.get_fileType(audioFileType)
        if audioFileID:
            item = mod.find_by_name(audioFileID)
            if item:
                return send_file(item.file_path, as_attachment=True)
            return errors['AudioNotExistsError'], 404
        else:
            #code to download all files
            zip_nm = mod.download_all()
            return send_file(zip_nm,
            mimetype = 'zip',
            attachment_filename= zip_nm,
            as_attachment = True)

    def delete(self, audioFileType,audioFileID):
        mod = Store.get_fileType(audioFileType)
        item = mod.find_by_name(audioFileID)
        if item:
            item.delete_from_db()
            mod.delete_file(audioFileID)
            return {'message': '{} Item deleted.'.format(audioFileID)}
        return errors['AudioNotExistsError'], 404


