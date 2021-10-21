def delete_playlist(db):
    database = db
    collection = database.playlists
    playlist = {"name": "teubidélice"}
    collection.delete_one(playlist)