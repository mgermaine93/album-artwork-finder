"""
Purpose of this file:
- Pass in the path to a song
- Return a string to use to search for the album cover using a search engine
"""

from tinytag import TinyTag


def create_search_term(path_to_song):
    tag = TinyTag.get(path_to_song)
    artist = tag.artist
    album = tag.album
    search_term = f"{album} {artist} Album Cover"
    return search_term


# create_search_term("/Users/mgermaine93/Desktop/test/02 Red Hawk Calling.m4a")

# This is what will be passed in
# "/Users/mgermaine93/Desktop/test/02 Red Hawk Calling.m4a"
