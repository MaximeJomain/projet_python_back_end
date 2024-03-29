from flask import Blueprint, request
from functions.connect_db import connect_db

app_create_playlist = Blueprint('app_create_playlist', __name__)


@app_create_playlist.route('/playlist/<id>', methods=['POST'])
def create_playlist(id):
    """ Function to create a new playlist
    :rtype: String
    :param id: id of the playlist you want to create
    :return: displays in console the playlist you created or displays a error message
    """

    playlist = {
        "_id": int(id),
        "playlist_name": request.get_json()['playlist_name'],
        "track_list": request.get_json()['track_list']
    }

    id_exists = False
    for i in connect_db().playlists.find({}, {"_id": 1}):
        if i["_id"] == int(id):
            id_exists = True

    if id_exists:
        return "The playlist ID already exist"

    else:
        return f"Status 201 Inserted playlist #{connect_db().playlists.insert_one(playlist).inserted_id}"
