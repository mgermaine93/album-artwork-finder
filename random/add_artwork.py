# https://www.codespeedy.com/add-album-art-to-an-mp3-file-in-python/

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
import os

audio_path = "/Users/mgermaine93/Desktop/Test-Music/01 Living In The Country.mp3"
picture_path = "/Users/mgermaine93/Desktop/Album-Art/0image.jpg"

audio = MP3(audio_path, ID3=ID3)
# adding ID3 tag if it is not present
try:
    audio.add_tags()
except error:
    pass
audio.tags.add(APIC(mime='image/jpeg', type=3, desc=u'Cover',
                    data=open(picture_path, 'rb').read()))
# edit ID3 tags to open and read the picture from the path specified and assign it
audio.save()  # save the current changes
