from markupsafe import escape
from flask import Blueprint, request
from functions.connect_db import connect_db

app_delete_playlist = Blueprint('app_delete_playlist', __name__)


@app_delete_playlist.route("/playlist/remove/<name>", methods=['DELETE'])
def delete_playlist(name):
    """this function delete a playlist from database

    :param name: the name of the playlist we want to delete
    :return: a status message
    """
    db = connect_db()  # The connection to database
    playlist_list = db.playlists.find({})
    if request.method == "DELETE":
        name = escape(name)
        for playlist in playlist_list:
            if playlist["name"] == name:
                collection = db.playlists
                collection.delete_one({'name': name})
                return f"delete {name}"
        return "err 404 this playlist doesn't exist"
