# https: // stackoverflow.com/questions/6171565/how-do-i-read-album-artwork-using-python

import eyed3
from mutagen.id3 import ID3, APIC, error
from mutagen.mp3 import MP3
from mutagen import File

# filename = "/Users/mgermaine93/Desktop/Test-Music/03 Dylan Thomas.mp3"
# album_art = "/Users/mgermaine93/Desktop/better oblivion community center.jpg"
filename = "/Users/mgermaine93/Desktop/Test-Music/01 Dragonfly.m4a"
album_art = "/Users/mgermaine93/Desktop/looking_wolf_artwork.jpg"

audio = MP3(filename, ID3=ID3)

# add ID3 tag if it doesn't exist
try:
    audio.add_tags()
except error:
    pass

try:
    file = File(filename)
    artwork = file.tags['APIC:'].data
    print("Track already has album artwork.")
# The code above will throw a KeyError if there is no value associated with "APIC:"
except KeyError:
    print("adding album artwork")
    audio.tags.add(
        APIC(
            encoding=3,  # 3 is for utf-8
            mime='image/jpeg',  # image/jpeg or image/png
            type=3,  # 3 is for the cover image
            desc=u'Cover',
            data=open(album_art, 'rb').read()
        )
    )
audio.save()

# # The below code also works
# audiofile = eyed3.load(filename)
# if (audiofile.tag == None):
#     audiofile.initTag()
# # Saves the image as the album artwork
# audiofile.tag.images.set(3, open(album_art, 'rb').read(), 'image/jpeg')
# audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
# #   #################
