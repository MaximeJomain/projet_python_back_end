from markupsafe import escape
from flask import Blueprint, request
from functions.connect_db import connect_db

app_delete_playlist = Blueprint('app_delete_playlist', __name__)


@app_delete_playlist.route("/delete/<name>", methods=['DELETE'])
def delete_playlist(name):
    db = connect_db()
    playlist_list = db.playlists.find({})
    if request.method == "DELETE":
        name = escape(name)
        for playlist in playlist_list:
            print(playlist["name"])
            if playlist["name"] == name:
                collection = db.playlists
                collection.delete_one({'name': name})
                return f"delete {name}"
        return "this playlist doesn't exist"
