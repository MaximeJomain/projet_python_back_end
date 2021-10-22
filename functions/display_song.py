from markupsafe import escape
from flask import Blueprint, request
from functions.connect_db import connect_db

app_display_song = Blueprint('app_display_song', __name__)


@app_display_song.route('/song/<id>', methods=['GET'])
def display_song(id):
    """ this function return a choosed songs

    :param id: the id of the song you want to display
    :return: all the information of the choosed songs
    """
    db = connect_db()
    song_list = db.songs.find({})
    if request.method == 'GET':
        id = str(escape(id))
        result = []
        for song in song_list:
            if str(song["_id"]) == id:
                result.append(f"id: {song['_id']} / auteur: {song['author']} / titre: {song['title']} / durée: {song['duration']}")
                return f"{result}"
        return " 200 this song doesn't exist"


