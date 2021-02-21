class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class AudioAlreadyExists(Exception):
    pass

class AudioNotExistsError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "AudioAlreadyExists": {
         "message": "Audio with given audioFileID already exists",
         "status": 400
     },
     "AudioNotExistsError": {
         "message": "Audio with given audioFileID doesn't exists",
         "status": 404
     }
}

