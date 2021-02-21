from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.song import SongModel


class Song(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('duration',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('upload_time',
                        type=str,
                        required=True,
                        help="Every item needs a upload_time."
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self,audioFileType, audioFileID):
        if SongModel.find_by_name(audioFileID):
            return {'message': "An item with name '{}' already exists.".format(audioFileID)}, 400

        data = Song.parser.parse_args()

        item = SongModel(audioFileID, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, **data)

        item.save_to_db()

        return item.json()


