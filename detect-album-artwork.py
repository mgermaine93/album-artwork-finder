# The purpose of this file (for now) is to detect any existing album artwork for a single .mp3.
# If there isn't any album artwork, then try adding it from a hardcoded file.

# https: // stackoverflow.com/questions/409949/how-do-you-embed-album-art-into-an-mp3-using-python

from mutagen import File
from mutagen.flac import Picture, FLAC
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error

file_name = "/Users/mgermaine93/Desktop/Test-Music/03 Dylan Thomas.mp3"
album_art = "/Users/mgermaine93/Desktop/better oblivion community center.jpg"

# Thanks to https: // stackoverflow.com/questions/409949/how-do-you-embed-album-art-into-an-mp3-using-python
audio = MP3(file_name, ID3=ID3)

# add ID3 tag if it doesn't exist
try:
    audio.add_tags()
except error:
    pass

file = File(file_name)
artwork = file.tags['APIC:'].data  # access APIC frame and grab the image

# If artwork already exists, we don't need to add it
if artwork:
    print("Artwork already exists!")
else:

    # Need to add logic for jpg, jpeg, and png
    audio.tags.add(
        APIC(
            encoding=3,  # 3 is for utf-8
            mime='image/jpg',  # image/jpeg or image/png
            type=3,  # 3 is for the cover image
            desc=u'Cover',
            data=open(album_art, 'rb').read()
        )
    )
    audio.save(v2_version=3)


# Alternative Solution, thanks to # https://stackoverflow.com/questions/38510694/how-to-add-album-art-to-mp3-file-using-python-3
# import eyed3
# file_name = "/Users/mgermaine93/Desktop/Test-Music/03 Dylan Thomas.mp3"
# album_art = "/Users/mgermaine93/Desktop/better oblivion community center.jpg"
# audiofile = eyed3.load(file_name)
# if (audiofile.tag == None):
#     audiofile.initTag()
# audiofile.tag.images.set(3, open(album_art, 'rb').read(), 'image/jpeg')
# audiofile.tag.save()
