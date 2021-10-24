from tinytag import TinyTag
from project.song import Song
from os import path
import os.path
import imagehash
from PIL import Image, ImageChops
from pathlib import Path
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from mutagen import File
from mutagen.mp4 import MP4, MP4Cover
from project.helpers import embed_album_artwork

file_path = '/Users/mgermaine93/Desktop/Test-Music/Dire Straits/Sultans Of Swing_ The Very Best Of Dire Straits/1-12 Calling Elvis.m4a'
file_path_to_image = '/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork/Dire Straits Sultans Of Swing: The Very Best Of Dire Straits Album Cover_new_artwork.jpeg'

# Might need to be refactored later...


def parse_artist(file_path_to_song):
    """
    Artist will (usually) be presented by the third-to-last item in the list
    """
    split_file = file_path_to_song.split('/')
    artist = split_file[-3]
    print(artist)
    return artist


def parse_album(file_path_to_song):
    """
    Album will (usually) be presented by the second-to-last item in the list
    """
    split_file = file_path_to_song.split('/')
    album = split_file[-2]
    print(album)
    return album


def create_search_term(file_path_to_song):
    """
    Takes in a file path to a song and returns a phrase that will be used to search for the song's corresponding album artwork.

    :param file_path_to_song:  a file path to an .mp3 or .m4a file.
    :type file_path_to_song: `string`, required.

    :return:  an object of type string that represents the search term to be used when finding album artwork for song file passed into the function.
    :rtype:  `string`.
    """
    if str(path.isfile(file_path_to_song)):
        song = TinyTag.get(file_path_to_song)
        print(song)
        try:
            album = song.album()
            print(album)
        except TypeError:
            print("TypeError has been caught for album.")
            album = parse_album(file_path_to_song)
        try:
            artist = song.artist()
            print(artist)
        except TypeError:
            print("TypeError has been caught for artist.")
            artist = parse_artist(file_path_to_song)
        term = f"{artist} {album} Album Cover"
        print(term)
        return term
    else:
        print("More work on this needs to be done.")
        return False


parse_artist(file_path)
parse_album(file_path)
create_search_term(file_path)
embed_album_artwork(file_path, file_path_to_image)
# https://stackoverflow.com/questions/38510694/how-to-add-album-art-to-mp3-file-using-python-3
