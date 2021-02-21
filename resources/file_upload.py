from flask_restful import Resource, reqparse
from flask import current_app as app,send_file
from models.song import SongModel
from models.podcast import PodCastModel
from models.audiobook import AudibookModel
from .serializers import songparser,podcastparser,audiobookparser,filetypeparser
from resources.errors import errors

class FileUpload(Resource):
    @classmethod
    def get_fileType(cls,audioFileType):
        if audioFileType == "song":
            mod = SongModel
        elif audioFileType == "podcast":
            mod = PodCastModel
        elif audioFileType == "audiobook":
            mod = AudibookModel
        return mod

    def post(self):
        in_file = filetypeparser.parse_args()
        audioFileType = in_file['audioFileType']
        audioFileID = in_file['audioFileID']
        mod = FileUpload.get_fileType(audioFileType)
        
        if mod.find_by_name(audioFileID):
            return errors['AudioAlreadyExists'],400
        
        data = mod.input_parser.parse_args()
        data['file_path'] = mod.save_update_file(audioFileID)

        item = mod(audioFileID, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def put(self):
        in_file = filetypeparser.parse_args()
        audioFileType = in_file['audioFileType']
        audioFileID = in_file['audioFileID']
        mod = FileUpload.get_fileType(audioFileType)

        data = mod.input_parser.parse_args()
        data['file_path'] = mod.save_update_file(audioFileID)

        item = mod.find_by_name(audioFileID)

        if item:
            item.name = data['name']
            item.duration = data['duration']
            item.upload_time = data['upload_time']
            item.file_path = data['file_path']
        else:
            item = mod(audioFileID, **data)
        # item.delete_from_db()
        item.save_to_db()

        return item.json()


