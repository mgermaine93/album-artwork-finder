# from artwork_grabber import get_album_artwork
from create_search_term import create_search_term
from detect_and_embed_album_artwork import detect_and_embed_album_artwork
import os

test_path = "/Users/mgermaine93/Desktop/test"
filename = "/Users/mgermaine93/Desktop/test/04 Tribute To The Ancestors.m4a"
album_art = "/Users/mgermaine93/Desktop/Album-Art/looking_wolf_artwork.jpg"


# Iterates over the files in the album and gets the search term
for song in os.listdir(test_path):
    song_path = (os.path.join(test_path, song))
    # create_search_term(song_path)
    detect_and_embed_album_artwork(song_path, album_art)

# Run the artwork grabber for each song

# create_search_term("/Users/mgermaine93/Desktop/test/02 Red Hawk Calling.m4a")
