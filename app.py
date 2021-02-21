from flask import Flask
from flask_restful import Api
from resources.store import Store
from resources.file_upload import FileUpload
from resources.errors import errors
from resources.routes import initialize_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app.config['SONG_UPLOAD_FOLDER'] = 'AudioFiles/songs'
app.config['PODCAST_UPLOAD_FOLDER'] = 'AudioFiles/podcast'
app.config['AUDIOFILES_UPLOAD_FOLDER'] = 'AudioFiles/audiobook'
app.secret_key = 'jose'



api = Api(app,errors=errors)


@app.before_first_request
def create_tables():
    db.create_all()

initialize_routes(api)



from db import db
db.init_app(app)
if __name__ == '__main__':
    
    app.run(port=5000, debug=True)
