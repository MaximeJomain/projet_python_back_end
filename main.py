from flask import Flask
import pymongo

app = Flask(__name__)


def main():
    client = pymongo.MongoClient(
        "mongodb+srv://coding:bad123@cluster0.jmgfz.mongodb.net/spotify_db?retryWrites=true&w=majority")
    db = client.test
    collection = db.collection0
    for i in range(1, 11):
        playlist = {
            "_id": i,
            "playlist_name": f"Playlist_name {i}",
        }
        playlist_id = collection.insert_one(playlist).inserted_id
        print(f"Inserted {playlist_id}: {playlist}")


if __name__ == '__main__':
    main()
