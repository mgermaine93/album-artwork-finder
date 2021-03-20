"""
Purpose of this file:
- Check to see whether or not an M4A file already has album artwork.
- If it does, print out a message saying it does and don't do anything else.
- If it doesn't, embed album artwork into the file.
"""

from mutagen.mp4 import MP4, MP4Cover
from mutagen.m4a import M4ACover
from mutagen import File

# filename = "/Users/mgermaine93/Desktop/Test-Music/01 Dragonfly.m4a"
# album_art = "/Users/mgermaine93/Desktop/looking_wolf_artwork.jpg"
filename = "/Users/mgermaine93/Desktop/Test-Music/01 Living In The Country.m4a"
album_art = "/Users/mgermaine93/Desktop/Album-Art/0image.jpg"

try:
    track = MP4(filename)
    tags = track.tags
    tags['covr']
    print("Track already has album artwork")
except KeyError:
    print("Track does not currently have album artwork")
    track = MP4(filename)

    # Thanks to: https://stackoverflow.com/questions/37897801/embedding-album-cover-in-mp4-file-using-mutagen
    with open(album_art, "rb") as f:
        track.tags["covr"] = [
            MP4Cover(f.read(), imageformat=MP4Cover.FORMAT_JPEG)
        ]
    track.save()
    print("artwork saved")

    # Alternate way:
    # covr = []
    # artworkfile = open(album_art, "rb").read()
    # covr.append(M4ACover(artworkfile, M4ACover.FORMAT_JPEG))
    # track.tags['covr'] = covr
    # track.save()
