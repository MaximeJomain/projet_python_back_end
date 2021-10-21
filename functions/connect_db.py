import pymongo


def connect_db():
    """ function to connect to database
    :return: return the database connection
    """
    client = pymongo.MongoClient(
        "mongodb+srv://coding:bad123@cluster0.jmgfz.mongodb.net/spotify_db?retryWrites=true&w=majority")
    db = client.spotify_db
    return db
