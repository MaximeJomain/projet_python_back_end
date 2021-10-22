from flask import Blueprint
from functions.connect_db import connect_db

app_display_playlist = Blueprint('app_display_playlist', __name__)


@app_display_playlist.route("/playlist", methods=['GET'])
def display_playlist():
    """This function display a list of playlists

    :return: list of all playlists
    """
    db = connect_db()
    collection = db.collection0

    for i in collection.find():
        return f"{i}"
