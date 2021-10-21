import pymongo
from flask import Flask

app = Flask(__name__)
path = "playlist/"

@app.route("/playlist/", methods=["GET"])
def display_playlist() :
    """This function display a list of playlists

    :return: list of all playlists
    """
    print("oui")