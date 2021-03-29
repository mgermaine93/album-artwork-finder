# from artwork_grabber import get_album_artwork
from create_search_term import create_search_term
from detect_and_embed_album_artwork import detect_and_embed_album_artwork
import os

root_path = "/Users/mgermaine93/Desktop/test"

# filename = "/Users/mgermaine93/Desktop/test/04 Tribute To The Ancestors.m4a"
# album_art = "/Users/mgermaine93/Desktop/Album-Art/looking_wolf_artwork.jpg"
# /Users/mgermaine93/Music/iTunes/iTunes Media/Music/Metheny _ Mehldau/Quartet/01 A Night Away.m4a


# Thanks to https://www.techiedelight.com/list-all-subdirectories-in-directory-python/
for artist in os.listdir(root_path):
    artist_path = os.path.join(root_path, artist)
    if os.path.isdir(artist_path):
        # print(f"The artist is: {artist_path}")
        for album in os.listdir(artist_path):
            album_path = os.path.join(artist_path, album)
            if os.path.isdir(album_path):
                # print(f"    The album is: {album_path}")
                for song in os.listdir(album_path):
                    song_path = os.path.join(album_path, song)
                    # print(f"        The song is: {song_path}")
                    # detect_and_embed_album_artwork(song_path, album_art)
                    term = create_search_term(song_path)

                    """
                    Steps to take next here include:
                    - Check whether or not the track has album artwork
                    - Create the search term if it doesn't have album artwork
                    - Run artwork grabber to retrieve and save artwork
                    """


# Run the artwork grabber for each song

# create_search_term("/Users/mgermaine93/Desktop/test/02 Red Hawk Calling.m4a")
