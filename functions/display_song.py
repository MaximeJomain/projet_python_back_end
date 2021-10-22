from markupsafe import escape
from flask import Blueprint, request
from functions.connect_db import connect_db

app_display_song = Blueprint('app_display_song', __name__)


@app_display_song.route('/song/<id>', methods=['GET'])
def display_song(id):
    db = connect_db()
    song_list = db.songs.find({})
    if request.method == 'GET':
        id = str(escape(id))
        for song in song_list:
            if str(song["_id"]) == id:
                print(song["_id"])
                print(song["author"])
                print(song["title"])
                print(song["duration"])


