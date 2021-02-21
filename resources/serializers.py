from flask_restful import reqparse,inputs,fields
import werkzeug
import datetime

def name(name_str):
    """Return name_str if valid, raise an exception in other case."""
    if name_str.strip() =='':
        raise ValueError('Cannot be Blank')
    elif not name_str.isalpha():
        raise ValueError('Should be string')
    elif len(name_str)>100:
        raise ValueError('Length should be less than 100 characters')
    else:
        return name_str

def duration(duration_str):
    duration_str = int(duration_str)
    """Return duration_str if valid, raise an exception in other case."""
    if int(duration_str) < 0 :
        raise ValueError('Duration cannot be negative')
    else:
        return duration_str

def participants(participants_str):
    """Return duration_str if valid, raise an exception in other case."""
    participants_str = participants_str.split(',')
    if not isinstance(participants_str, list):
        raise ValueError('Should be List')
    elif len(participants_str)>10:
        raise ValueError('Maximum of 10 participants possible')
    elif [li for li in participants_str  if not li.isalpha()]:
        raise ValueError('List should contain only strings')
    elif [li for li in participants_str  if len(li) > 100]:
        raise ValueError('List should contain strings not more than 100 characters')
    else:
        return participants_str

def upload_time(u_dt):
    date_time_obj = datetime.datetime.strptime(u_dt, '%Y-%m-%dT%H:%M:%S')
    if date_time_obj < datetime.datetime.now():
        raise ValueError('Upload Time cannot be in the past')
    return date_time_obj


songparser = reqparse.RequestParser()
fileparser = reqparse.RequestParser()
filetypeparser = reqparse.RequestParser()
songparser.add_argument('name',
                    type=name,
                    required=True,
                    help="Name of Song : {error_msg}"
                    )
songparser.add_argument('duration',
                    type=duration,
                    required=True,
                    help="Duration in number of seconds : {error_msg} "
                    )
songparser.add_argument('upload_time',
                    type=upload_time,
                    required=True,
                    help="Upload time : {error_msg}"
                    )

fileparser.add_argument('file',
                    type=werkzeug.datastructures.FileStorage,
                    location = 'files',
                    required=True,
                    help="File : {error_msg}"
                    )
                    
filetypeparser.add_argument('audioFileType',
                    type=str,
                    required=True,
                    help="Audio File Type : {error_msg}"
                    )
filetypeparser.add_argument('audioFileID',
                    type=int,
                    required=True,
                    help="Audio File ID : {error_msg}"
                    )

podcastparser = reqparse.RequestParser()
podcastparser.add_argument('name',
                    type=name,
                    required=True,
                    help="Name of Podcast : {error_msg}"
                    )
podcastparser.add_argument('duration',
                    type=duration,
                    required=True,
                    help="Duration in number of seconds : {error_msg} "
                    )
podcastparser.add_argument('upload_time',
                    type=upload_time,
                    required=True,
                    help="Upload time : {error_msg}"
                    )
podcastparser.add_argument('host',
                    type=name,
                    required=True,
                    help="Host : {error_msg}"
                    )
podcastparser.add_argument('participants',
                    type=participants,
                    help="Participants : {error_msg}"
                    )


audiobookparser = reqparse.RequestParser()
audiobookparser.add_argument('name',
                    type=name,
                    required=True,
                    help="Title of Audiobook : {error_msg}"
                    )
audiobookparser.add_argument('author',
                    type=name,
                    required=True,
                    help="Author of the Title : {error_msg} "
                    )
audiobookparser.add_argument('narrator',
                    type=name,
                    required=True,
                    help="Narrator : {error_msg} "
                    )
audiobookparser.add_argument('duration',
                    type=duration,
                    required=True,
                    help="Duration in number of seconds : {error_msg} "
                    )
audiobookparser.add_argument('upload_time',
                    type=upload_time,
                    required=True,
                    help="Upload time : {error_msg}"
                    )

