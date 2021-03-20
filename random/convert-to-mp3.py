"""
Purpose of this code:

If the file is not MP3 (e.g., M4A):

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
song_name = "01 Living In The Country.m4a"
song_name_minus_file_type = song_name[0:-4]
song_file_type = song_name[-4:]
song_full_name = f"{song_directory}{song_name}"
song_full_path_minus_file_type = f"{song_directory}{song_name_minus_file_type}"
mp3_file_path = f"{song_directory}{song_name_minus_file_type}.mp3"


def get_track_info(self, track_file_path):
    # This grabs the track information from the existing file before it is converted
    m4a = TinyTag.get(track_file_path)

    album = m4a.album
    # album_artist = m4a.albumartist
    title = m4a.title
    artist = m4a.artist
    composer = m4a.composer
    genre = m4a.genre
    year = m4a.year
    track_number = m4a.track
    track_total = m4a.track_total
    disc_number = m4a.disc
    disc_total = m4a.disc_total
    duration = m4a.duration

    return album, title, artist, composer, genre, year, track_number, disc_number


def convert_m4a_to_mp3(self, track_file_path_minus_file_type):
    # This part does the conversion from m4a to mp3
    m4a_audio = AudioSegment.from_file(
        f"{track_file_path_minus_file_type}.m4a", format="m4a")
    m4a_audio.export(
        f"{track_file_path_minus_file_type}.mp3", format="mp3")


def assign_metadata_to_track(self, track_file_path, track_full_path_minus_file_type):

    info = self.get_track_info(track_file_path)
    # This assigns the m4a track field values to the new mp3
    mp3 = EasyID3(f"{track_full_path_minus_file_type}.mp3")

    # Verify that there are values to assign to the new mp3 and assign them
    if info.album is not None:
        mp3['album'] = album
    if info.title is not None:
        mp3['title'] = title
    if info.artist is not None:
        mp3['artist'] = artist
    if info.composer is not None:
        mp3['composer'] = composer
    if genre is not None:
        mp3['genre'] = genre
    if year is not None:
        mp3['date'] = year
    if track_number is not None and track_total is not None:
        EasyID3.RegisterTextKey('track total', 'TRCK')
        mp3['track total'] = f"{track_number}/{track_total}"
    if disc_number is not None and disc_total is not None:
        EasyID3.RegisterTextKey('disc total', 'TPOS')
        mp3['disc total'] = f"{disc_number}/{disc_total}"

    mp3.save(v2_version=3)

    return album, title, artist, composer, genre, year, track_number, disc_number


# Get track info with the full path name
get_track_info(song_full_name)

# M4A -> MP3
convert_m4a_to_mp3(song_full_path_minus_file_type)

# Assign M4A field values to MP3 field value
assign_metadata_to_track(song_full_name, song_full_path_minus_file_type)

# Get MP3 track info with the full path name
get_track_info(mp3_file_path)

# mp3_path = f"{song_directory}{song_name_minus_file_type}.mp3"
# get_album_info(mp3_path)

# print(song_full_name)
# This was helpful:  https://id3.org/id3v2.4.0-frames
