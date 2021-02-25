# The purpose of this file is to convert a hard-coded media file (m4a for now) to mp3.

from pydub import AudioSegment
from tinytag import TinyTag
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

song_directory = "/Users/mgermaine93/Desktop/Test-Music/"
song_full_name = "03 Dylan Thomas.m4a"
song_name = song_full_name[0:-4]
song_file_type = song_full_name[-4:]

print(f"{song_directory}{song_name}{song_file_type}")

# This captures the album name, track name, etc. before the file is converted
audio = TinyTag.get(f"{song_directory}{song_name}{song_file_type}")
# artist = audio.artist
# print(artist)

# This part does (should do) the conversion from m4a to mp3
m4a_audio = AudioSegment.from_file(f"{song_directory}{song_full_name}", format="m4a")
m4a_audio.export(f"{song_directory}{song_name}.mp3", format="mp3")

# # song_properties = {
# #     "Album": audio.album,
# #     "Artist": audio.artist,
# #     "Title": audio.title,
# #     "Musical genre": audio.genre,
# #     "Authors": audio.albumartist,
# #     "Composer": audio.composer,
# #     "Year recorded": audio.year,
# # }