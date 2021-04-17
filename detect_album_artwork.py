"""
Purpose of this file:
- Check to see whether or not an M4A or MP3 file already has album artwork.
- If it already has album artwork, print out a message saying it so and return True.
- If it doesn't already have album artwork, print out a message saying it so and return False.
"""

from mutagen.mp4 import MP4, MP4Cover
from mutagen.m4a import M4ACover
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from mutagen import File


def detect_album_artwork(filename):

    last_four = filename[-4:]
    # print(last_four)
    # Checks the string version of the filename
    if last_four == ".m4a":
        # print("File is an M4A")
        try:
            track = MP4(filename)
            tags = track.tags
            tags['covr']
            # print("M4A track already has album artwork")
            return True
        except KeyError:
            print("M4A track needs album artwork")
            return False

    elif last_four == ".mp3":
        # print("File is an MP3")
        try:
            mp3 = MP3(filename, ID3=ID3)
            tags = mp3.tags
            tags['covr']
            # print("MP3 track already has album artwork")
            return True
        except KeyError:
            print("MP3 track needs album artwork")
            return False
    else:
        print("Filename name is not M4A nor MP3")
        return False


# detect_album_artwork("/Users/mgermaine93/Desktop/test/Bill Evans/For Lovers/07 Lover Man.m4a")
