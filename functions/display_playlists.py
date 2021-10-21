import pymongo
from flask import Flask

app = Flask(__name__)
path = "playlist/"


@app.route("/playlist/", methods=["GET"])
def display_playlist(db):
    """This function display a list of playlists

    :param database connection

    :return: list of all playlists
    """

    col = db["playlists"]

    for x in col.find():
        print(x)
