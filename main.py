from flask import Flask
from Functions.connect_db import connect_db

import pymongo

app = Flask(__name__)

if __name__ == "__main__" :

    connect_db()
