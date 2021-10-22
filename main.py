from flask import Flask
from functions.create_playlist import app_create_playlist
from functions.display_playlist import app_display_playlist
from functions.update_playlist import app_update_playlist

app = Flask(__name__)
app.register_blueprint(app_create_playlist)
app.register_blueprint(app_display_playlist)
app.register_blueprint(app_update_playlist)


@app.route('/')
def main():
    return "in main"
