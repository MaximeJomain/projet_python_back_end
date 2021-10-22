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
    name = request_data['playlist_name']
    db = connect_db()
    collection = db.playlists
    playlist_list = db.playlists.find({}, {"_id": 1})
    playlist_id = int(id)

    if request.method == "PATCH":
        for playlist in playlist_list:
            if (playlist["_id"]) == playlist_id:
                collection.update_one({"_id": playlist_id}, {"$set": {"playlist_name": name}})
                return "status 200"
        return "status 304"