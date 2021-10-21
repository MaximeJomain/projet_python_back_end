import pymongo


def connect_db():
    client = pymongo.MongoClient(
        "mongodb+srv://coding:bad123@cluster0.jmgfz.mongodb.net/spotify_db?retryWrites=true&w=majority")
    db = client.spotify_db
    return db

