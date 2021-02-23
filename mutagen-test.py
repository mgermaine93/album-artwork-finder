# This converts an m4a to an mp3 successfully, but does not preserve any metadata...

from pydub import AudioSegment
from tinytag import TinyTag

song_directory = "/Users/mgermaine93/Desktop/Test-Music/"
song = "03 Dylan Thomas.m4a"

# This captures the album name, track name, etc. before the file is converted
audio = TinyTag.get(f"{song_directory}{song}")

song_properties = {
    "Album": audio.album,
    "Artist": audio.artist,
    "Title": audio.title,
    "Musical genre": audio.genre,
    "Authors": audio.albumartist,
    "Composer": audio.composer,
    "Year recorded": audio.year,
}

print(song_properties)

# m4a_audio = AudioSegment.from_file(f"{song_directory}03 Dylan Thomas.m4a", format="m4a")
# # raw_audio = AudioSegment.from_file(f"{song_directory}03 Dylan Thomas.m4a", format="raw", frame_rate=44100, channels=2, sample_width=2)
# m4a_audio.export(f"{song_directory}audio1.mp3", format="mp3")
# # raw_audio.export(f"{song_directory}audio2.mp3", format="mp3")

