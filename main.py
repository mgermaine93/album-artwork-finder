"""
Purpose of this file:
- Loops through a directory containing artists, albums, and songs (in that order).
- Perform the main functionality of the project.
"""

from pathlib import Path
from create_search_term import create_search_term
from detect_album_artwork import detect_album_artwork
from artwork_grabber import get_album_artwork
from embed_album_artwork import embed_album_artwork
import os

root_path = "/Users/mgermaine93/Desktop/test"
print(os.listdir(root_path))

artists = [
    file for file in Path(root_path).iterdir() if not file.name.startswith(".")
]

# Thanks to https://www.techiedelight.com/list-all-subdirectories-in-directory-python/
for artist in artists:
    artist_path = os.path.join(root_path, artist)
    print(f"artist path is here: {artist_path}")
    if os.path.isdir(artist_path):
        print(f"The artist is: {artist_path}")
        albums = [
            file for file in Path(artist_path).iterdir() if not file.name.startswith(".")
        ]
        for album in albums:
            album_path = os.path.join(artist_path, album)
            if os.path.isdir(album_path):
                print(f"album path is here: {album_path}")
                # print(f"    The album is: {album_path}")
                songs = [
                    file for file in Path(album_path).iterdir() if not file.name.startswith(".")
                ]
                for song in songs:
                    song_path = os.path.join(album_path, song)
                    print(song_path)
                    # print(f"        The song is: {song_path}")
                    if not detect_album_artwork(song_path):
                        # Get the search term
                        print("Getting search term")
                        search_term = create_search_term(song_path)
                        print(search_term)
                        # Retrieve an image using the search term
                        # print("Retrieving artwork")
                        get_album_artwork(search_term, save_folder)
                        # Add the artwork to the track
                        print("Adding artwork")
                        embed_album_artwork(
                            song_path, "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork/artwork.jpg")

print("done")
