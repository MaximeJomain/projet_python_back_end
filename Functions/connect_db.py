import pymongo


def connect_db():
    client = pymongo.MongoClient(
        "mongodb+srv://coding:bad123@cluster0.jmgfz.mongodb.net/spotify_db?retryWrites=true&w=majority")
    db = client.test
    collection = db.collection0
    for i in range(1, 2):
        playlist = {
            "_id": i,
            "playlist_name": f"Playlist_name {i}",
        }
        playlist_id = collection.insert_one(playlist).inserted_id
        print(f"Inserted {playlist_id}: {playlist}")
