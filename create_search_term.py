"""
Purpose of this file:
- Pass in the path to a song
- Return the name of the album the song belongs to
"""

from tinytag import TinyTag


def create_search_term(path_to_song):
    tag = TinyTag.get(path_to_song)
    artist = tag.artist
    album = tag.album
    search_term = f"{album} {artist} Album Cover"
    print(search_term)
    return search_term


create_search_term("/Users/mgermaine93/Desktop/test/02 Red Hawk Calling.m4a")

# This is what will be passed in
# "/Users/mgermaine93/Desktop/test/02 Red Hawk Calling.m4a"
