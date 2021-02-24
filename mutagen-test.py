# This converts an m4a to an mp3 successfully, but does not preserve any metadata...

from pydub import AudioSegment
from tinytag import TinyTag
from mutagen.easyid3 import EasyID3

song_directory = "/Users/mgermaine93/Desktop/Test-Music/"
song = "03 Dylan Thomas.m4a"

# This captures the album name, track name, etc. before the file is converted
audio = TinyTag.get(f"{song_directory}{song}")

# song_properties = {
#     "Album": audio.album,
#     "Artist": audio.artist,
#     "Title": audio.title,
#     "Musical genre": audio.genre,
#     "Authors": audio.albumartist,
#     "Composer": audio.composer,
#     "Year recorded": audio.year,
# }

artist = audio.artist
print(artist)


# This part does (should do) the conversion from m4a to mp3
m4a_audio = AudioSegment.from_file(f"{song_directory}03 Dylan Thomas.m4a", format="m4a")
m4a_audio.export(f"{song_directory}audio1.mp3", format="mp3")

# Trying to assign hardcoded values to the converted mp3, but this isn't working quite yet.
# Will eventually need to find a way to make this dynamic as well
mp3 = EasyID3(f"{song_directory}audio1.mp3")
if mp3:
    print("yo")
    mp3["Album"] = u"Better Oblivion Community Center"
    mp3["Title"] = u"Dylan Thomas"
    mp3["Genre"] = u"Indie Rock"
    mp3["Author"] = u"Better Oblivion Community Center"
    mp3["Artist"] = u"Better Oblivion Community Center"
    mp3["Composer"] = u"Conor Oberst/Phoebe Bridgers"
    mp3["Date"] = u"2019" # this works, but does not show up in the file GUI
    mp3.save()

# Might need later, not sure...
# # raw_audio = AudioSegment.from_file(f"{song_directory}03 Dylan Thomas.m4a", format="raw", frame_rate=44100, channels=2, sample_width=2)
# # raw_audio.export(f"{song_directory}audio2.mp3", format="mp3")