from mutagen.mp4 import MP4, MP4Cover
from mutagen import File
from mutagen.id3 import ID3, APIC, error
from mutagen.mp3 import MP3
from pathlib import Path
from PIL import Image, ImageChops
import imagehash
import os.path
from os import path
from song import Song


def create_search_term(file_path_to_song):
    """
    Takes in a file path to a song and returns a phrase that will be used to search for the song's corresponding album artwork.

    :param file_path_to_song:  a file path to an .mp3 or .m4a file.
    :type file_path_to_song: `str`, required.

    :return:  an object of type string that represents the search term to be used when finding album artwork for song file passed into the function.
    :rtype:  `string`.
    """
    if str(path.isfile(file_path_to_song)):
        song = Song(file_path_to_song)
        album = song.get_album()
        artist = song.get_artist()
        term = f"{artist} {album} Album Cover"
        return term
    else:
        return False


def detect_album_artwork(file_path_to_song):
    """
    Takes in a file path to a song and returns a boolean to determine whether or not the file already has album artwork associated with it.

    :param file_path_to_song:  a file path to an .mp3 or .m4a file.
    :type file_path_to_song: `str`, required.

    :return:  an object of type boolean that represents whether or not the song file passed into the function currently has album artwork associated with it.  `True` indicates that artwork is already associated with the song, whereas `False` indicates that artwork is not already associated with the song.
    :rtype:  `boolean`.
    """

    if str(path.isfile(file_path_to_song)):

        file_type = Path(file_path_to_song).suffix.lower()

        if file_type == ".m4a":
            try:
                m4a = MP4(file_path_to_song)
                tags = m4a.tags
                tags['covr']
                print("M4A track has album artwork")
                return True
            except KeyError:
                print("M4A track needs album artwork")
                return False
        elif file_type == ".mp3":
            try:
                mp3 = MP3(file_path_to_song, ID3=ID3)
                tags = mp3.tags
                tags['covr']
                print("MP3 track has album artwork")
                return True
            except KeyError:
                print("MP3 track needs album artwork")
                return False
        else:
            print("Filename name is not M4A nor MP3.")
            return False
    else:
        print("Not a valid file path.")
        return False


def embed_album_artwork(file_path_to_song, file_path_to_image):
    """
    Takes in a file path to a song AND a file path to an image and saves the image as the album artwork to the song.

    :param file_path_to_song:  a file path to an .mp3 or .m4a file.
    :type file_path_to_song: `str`, required.
    :param file_path_to_image:  a file path to an image.
    :type file_path_to_image: `str`, required.

    :return:  an object of type boolean that represents whether or not the image was successfully saved as the album artwork to a song file.  `True` indicates that the image was successfully saved, whereas `False` indicates that the image was not successfully saved.
    :rtype:  `boolean`.
    """

    file_type = Path(file_path_to_song).suffix.lower()
    print(file_type)

    if file_type == ".m4a":
        m4a = MP4(file_path_to_song)

        # Thanks to: https://stackoverflow.com/questions/37897801/embedding-album-cover-in-mp4-file-using-mutagen
        with open(file_path_to_image, "rb") as f:
            m4a.tags["covr"] = [
                MP4Cover(f.read(), imageformat=MP4Cover.FORMAT_JPEG)
            ]
            m4a.save()
            print("Artwork saved")
            return True
    elif file_type == ".mp3":
        # Thanks to https://stackoverflow.com/questions/409949/how-do-you-embed-album-art-into-an-mp3-using-python
        mp3 = MP3(file_path_to_song, ID3=ID3)
        mp3.tags.add(
            APIC(
                encoding=3,  # 3 is for utf-8
                mime='image/jpg',  # image/jpeg or image/png
                type=3,  # 3 is for the cover image
                desc=u'Cover',
                data=open(file_path_to_image, "rb").read()
            )
        )
        mp3.save()
        print("Artwork added")
        return True
    else:
        print("Filename name is not M4A nor MP3")
        return False

# This needs to be worked on a bit more...
# Thanks to https://stackoverflow.com/questions/52736154/how-to-check-similarity-of-two-images-that-have-different-pixelization


def compare_artwork(existing_artwork, found_artwork):
    """
    Takes in the file paths to two images (each is a string) and returns a boolean determining whether they are similar (True) or not (False).
    """
    hash0 = imagehash.average_hash(Image.open(existing_artwork))
    hash1 = imagehash.average_hash(Image.open(found_artwork))
    cutoff = 5  # maximum bits that could be difference between the hashes.
    if hash0 - hash1 < cutoff:
        print("Images are similar")
        return True
    else:
        print("Images are not similar")
        return False


# detect_album_artwork("/Users/mgermaine93/Desktop/03 Dylan Thomas.m4a")
# compare_artwork("../artwork/artwork1.jpg", "../artwork/artwork3.jpg")
