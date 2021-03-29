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

# filename = "/Users/mgermaine93/Desktop/Test-Music/01 Dragonfly.m4a"
# album_art = "/Users/mgermaine93/Desktop/looking_wolf_artwork.jpg"


def detect_and_embed_album_artwork(filename):

    last_four = filename[-4:]
    print(last_four)
    # Checks the string version of the filename
    if last_four == ".m4a":
        print("File is an M4A")
        try:
            track = MP4(filename)
            tags = track.tags
            tags['covr']
            print("M4A track already has album artwork")
            return True
        except KeyError:
            print("M4A track needs album artwork")
            return False

    elif last_four == ".mp3":
        print("File is an MP3")
        try:
            mp3 = MP3(filename, ID3=ID3)
            tags = mp3.tags
            tags['covr']
            print("MP3 track already has album artwork")
            return True
        except KeyError:
            print("MP3 track needs album artwork")
            return False
    else:
        print("Filename name is not M4A nor MP3")


detect_and_embed_album_artwork(
    "/Users/mgermaine93/Desktop/test/Bill Evans/For Lovers/06 It Must Be Love.m4a")

# detect_and_embed_album_artwork("/Users/mgermaine93/Desktop/test/04 Tribute To The Ancestors.m4a","/Users/mgermaine93/Desktop/Album-Art/looking_wolf_artwork.jpg")

# detect_and_embed_album_artwork(filename)
# Alternate way:
# covr = []
# artworkfile = open(album_art, "rb").read()
# covr.append(M4ACover(artworkfile, M4ACover.FORMAT_JPEG))
# track.tags['covr'] = covr
# track.save()
