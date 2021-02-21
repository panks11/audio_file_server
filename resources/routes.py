from .store import Store
from .file_upload import FileUpload

def initialize_routes(api):
    api.add_resource(FileUpload, '/audio')
    api.add_resource(Store,'/audio/<audioFileType>', '/audio/<audioFileType>/<audioFileID>')