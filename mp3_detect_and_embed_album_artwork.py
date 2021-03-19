"""
Purpose of this file:
- Check to see whether or not an MP3 file already has album artwork.
- If it does, print out a message saying it does and don't do anything else.
- If it doesn't, embed album artwork into the file.
"""

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error

filename = "/Users/mgermaine93/Desktop/Test-Music/01 Living In The Country.mp3"
album_art = "/Users/mgermaine93/Desktop/Album-Art/0image.jpg"

try:
    mp3 = MP3(filename, ID3=ID3)
    tags = mp3.tags
    tags['covr']
    print("Track already has album artwork")
except KeyError:
    print("Track needs artwork")
    # Thanks to https://stackoverflow.com/questions/409949/how-do-you-embed-album-art-into-an-mp3-using-python
    mp3 = MP3(filename, ID3=ID3)
    mp3.tags.add(
        APIC(
            encoding=3,  # 3 is for utf-8
            mime='image/jpg',  # image/jpeg or image/png
            type=3,  # 3 is for the cover image
            desc=u'Cover',
            data=open(album_art, "rb").read()
        )
    )
    print("Artwork added")
    mp3.save()
