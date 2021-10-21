from flask import Flask
from functions.create_playlist import app_create_playlist

app = Flask(__name__)
app.register_blueprint(app_create_playlist)


@app.route('/')
def main():
    return "in main"
