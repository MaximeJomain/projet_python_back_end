from flask import Blueprint, request
from functions.connect_db import connect_db

app_create_playlist = Blueprint('app_create_playlist', __name__)


@app_create_playlist.route('/createPlaylist', methods=['POST'])
def create_playlist():
    if request.method == 'POST':
        name = request.form.get('name')
        db = connect_db()
        collection = db.playlists
        playlist = {
            "name": name
        }
        playlist_id = collection.insert_one(playlist).inserted_id
        return f"Inserted {playlist_id}: {playlist}"
