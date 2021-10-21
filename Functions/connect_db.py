import pymongo


def connect_db():
    client = pymongo.MongoClient(
        "mongodb+srv://coding:factory@cluster0.8mkxa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    collection = db.collection0
    for i in range(1, 3):
        playlist = {
            "id_playlist": i,
            "playlist_name": f"Playlist_name {i}",
            "tracks": {"id_track1": i,
                        "id_track2": i+1}
        }
        playlist_id = collection.insert_one(playlist).inserted_id
        print(f"Inserted {playlist_id}: {playlist}")
