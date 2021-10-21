from flask import Flask
from functions.connect_db import connect_db
from functions.create_playlist import create_playlist

import pymongo

app = Flask(__name__)

if __name__ == "__main__":
    create_playlist(connect_db(), "kebab")
