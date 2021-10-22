from flask import Flask
from functions.create_playlist import app_create_playlist
from functions.display_playlist import app_display_playlist
from functions.delete_playlist import app_delete_playlist

app = Flask(__name__)
app.register_blueprint(app_create_playlist)
app.register_blueprint(app_delete_playlist)
app.register_blueprint(app_display_playlist)


@app.route('/')
def main():
    return "in main"
