"""
Purpose of this code:

If the file is not MP3:

- Capture the metadata tags
- Convert the file to MP3
- Assign the metadata tags to the MP3 file
- Remove the old file (eventually)
"""

from pydub import AudioSegment
from tinytag import TinyTag
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import mutagen

song_directory = "/Users/mgermaine93/Desktop/Test-Music/"
# song_name = "03 Dylan Thomas.m4a"
song_name = "01 Dragonfly.m4a"
song_name_minus_file_type = song_name[0:-4]
song_file_type = song_name[-4:]
song_full_name = f"{song_directory}{song_name}"

# This grabs the track information from the existing file before it is converted
mp3 = TinyTag.get(f"{song_full_name}")

album = mp3.album
# album_artist = mp3.albumartist
title = mp3.title
artist = mp3.artist
composer = mp3.composer
genre = mp3.genre
year = mp3.year
track_number = mp3.track
track_total = mp3.track_total
disc_number = mp3.disc
disc_total = mp3.disc_total
duration = mp3.duration
# print(f"This is the duration of the m4a: {duration}")

# This part does the conversion from m4a to mp3
m4a_audio = AudioSegment.from_file(
    f"{song_full_name}", format="m4a")
m4a_audio.export(
    f"{song_directory}{song_name_minus_file_type}.mp3", format="mp3")

# This assigns the m4a track field values to the new mp3
mp3 = EasyID3(f"{song_directory}{song_name_minus_file_type}.mp3")

mp3['album'] = album
mp3['title'] = title
mp3['artist'] = artist
mp3['composer'] = composer
mp3['genre'] = genre
mp3['date'] = year
EasyID3.RegisterTextKey('track total', 'TRCK')
mp3['track total'] = f"{track_number}/{track_total}"
EasyID3.RegisterTextKey('disc total', 'TPOS')
mp3['disc total'] = f"{disc_number}/{disc_total}"

mp3.save(v2_version=3)

# Get the properties of the mp3
new_song = TinyTag.get(f"{song_directory}{song_name_minus_file_type}.mp3")

new_duration = new_song.duration
print(f"This is the duration of the mp3: {new_duration}")

# print(song_full_name)
# This was helpful:  https://id3.org/id3v2.4.0-frames
