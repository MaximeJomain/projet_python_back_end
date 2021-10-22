from flask import Blueprint, request
from functions.connect_db import connect_db
from markupsafe import escape

app_update_playlist = Blueprint('app_update_playlist', __name__)


@app_update_playlist.route("/playlist/<id>", methods=['PATCH'])
def update_playlist(id):
    """This function update a playlist
    :param id: id of the playlist you want to update
    :return: playlist updated
    """

    request_data = request.get_json()
    name = request_data['name']
    db = connect_db()
    playlist_list = db.playlists.find({})
    collection = db.playlists
    if request.method == "PATCH":
        playlist_id = str(escape(id))
        for playlist in playlist_list:
            print(playlist["_id"])
            print(playlist_id)
            if str(playlist["_id"]) == playlist_id:
                print(playlist)
                collection.update_one({"_id": playlist_id}, {"$set": {"name": name}})
                playlist.update({"$set": {"name": name}})
                return playlist
        return "sorti de la boucle"
