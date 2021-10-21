def create_playlist(db, name):
    database = db
    collection = database.playlists
    playlist = {
        "name": name
    }
    playlist_id = collection.insert_one(playlist).inserted_id
    print(f"Inserted {playlist_id}: {playlist}")


if __name__ == "__create_playlist__":
    create_playlist("kebab")