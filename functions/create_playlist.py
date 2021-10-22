from flask import Blueprint, request
from functions.connect_db import connect_db

app_create_playlist = Blueprint('app_create_playlist', __name__)


@app_create_playlist.route('/playlist/<id>', methods=['POST'])
def create_playlist(id):
    """ Function to create a new playlist
    :rtype: String
    :param id: id of the playlist you want to create
    :return: display in console the playlist you created or a error message
    """
    if request.method == 'POST':
        request_data = request.get_json()
        request_id = int(id)
        name = request_data['name']
        db = connect_db()
        collection = db.playlists
        playlist = {
            "_id": request_id,
            "name": name
        }
        id_exists = False
        for i in collection.find({}, {"_id": 1}):
            if i["_id"] == request_id:
                id_exists = True

        if id_exists:
            return "The playlist ID already exist"

        else:
            playlist_id = collection.insert_one(playlist).inserted_id
            return f"Inserted {playlist_id}: {playlist}"
