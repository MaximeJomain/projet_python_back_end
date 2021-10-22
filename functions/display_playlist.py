from flask import Blueprint
from functions.connect_db import connect_db

app_display_playlist = Blueprint('app_display_playlist', __name__)


@app_display_playlist.route("/playlist", methods=['GET'])
def display_playlist():
    """This function display a list of playlists

    :return: list of all playlists
    """
    db = connect_db()
    collection = db.playlists
    result = []

    for i in collection.find():
        result.append(f"Playlist {i['_id']} = {i['playlist_name']}")
    if len(result) == 0 :
        return "status 200 : nombre de ressource retouné 0"
    else:
        return f"nombre de ressources retournées {len(result)} {result}"
