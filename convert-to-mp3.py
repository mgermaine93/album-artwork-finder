# The purpose of this file is to convert a hard-coded media file (m4a for now) to mp3 and preserve as much original track metadata as possible (not including the album artwork).

from pydub import AudioSegment
from tinytag import TinyTag
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import mutagen

song_directory = "/Users/mgermaine93/Desktop/Test-Music/"
song_name = "03 Dylan Thomas.m4a"
song_name_minus_file_type = song_name[0:-4]
song_file_type = song_name[-4:]
song_full_name = f"{song_directory}{song_name}"
print(song_full_name)

# This grabs the track information from the existing file before it is converted


def convert_m4a_to_mp3(song):

    audio = TinyTag.get(f"{song_full_name}")

    album = audio.album         # album as string
    print(f"This is the album: {album}")
    album_artist = audio.albumartist   # album artist as string
    print(f"This is the album artist: {album_artist}")
    artist = audio.artist        # artist name as string
    print(f"This is the artist: {artist}")
    audio_offset = audio.audio_offset  # number of bytes before audio data begins
    print(f"This is the audio offset: {audio_offset}")
    bitrate = audio.bitrate       # bitrate in kBits/s
    print(f"This is the bitrate: {bitrate}")
    comment = audio.comment       # file comment as string
    print(f"This is the comment: {comment}")
    composer = audio.composer      # composer as string
    print(f"This is the composer: {composer}")
    disc_number = audio.disc          # disc number
    print(f"This is the disc: {disc_number}")
    disc_total = audio.disc_total    # the total number of discs
    print(f"This is the disc total: {disc_total}")
    duration = audio.duration      # duration of the song in seconds
    print(f"This is the duration: {duration}")
    filesize = audio.filesize      # file size in bytes
    print(f"This is the filesize: {filesize}")
    genre = audio.genre         # genre as string
    print(f"This is the genre: {genre}")
    samplerate = audio.samplerate    # samples per second
    print(f"This is the samplerate: {samplerate}")
    title = audio.title         # title of the song
    print(f"This is the title: {title}")
    track_number = audio.track         # track number as string
    print(f"This is the track number: {track_number}")
    track_total = audio.track_total   # total number of tracks as string
    print(f"This is the track total: {track_total}")
    year = audio.year          # year or data as string
    print(f"This is the year: {year}")

    # This part does (should do) the conversion from m4a to mp3
    m4a_audio = AudioSegment.from_file(
        f"{song_full_name}", format="m4a")
    m4a_audio.export(
        f"{song_directory}{song_name_minus_file_type}.mp3", format="mp3")

    # Might need error handling here like this:  https://stackoverflow.com/questions/42231932/writing-id3-tags-using-easyid3

    # This assigns the m4a track field values to the new mp3
    try:
        mp3 = EasyID3(f"{song_directory}{song_name_minus_file_type}.mp3")
    except:
        mp3 = mutagen.File(path, easy=True)
        mp3.add_tags()

    mp3['album'] = album
    # mp3['albumartist'] = album_artist
    mp3['artist'] = artist
    mp3['composer'] = composer
    mp3['discnumber'] = disc_number
    mp3['tracknumber'] = track_number
    mp3['length'] = duration
    mp3['genre'] = genre
    mp3['title'] = title
    mp3['date'] = year

    # # Still need to figure these out
    # audio_offset = audio.audio_offset  # number of bytes before audio data begins
    # bitrate = audio.bitrate       # bitrate in kBits/s
    # comment = audio.comment       # file comment as string
    # disc_total = audio.disc_total    # the total number of discs
    # filesize = audio.filesize      # file size in bytes
    # samplerate = audio.samplerate    # samples per second
    # track_total = audio.track_total   # total number of tracks as string

    mp3.save()
    print(mp3)


convert_m4a_to_mp3(
    f"{song_full_name}")

# album, title, musical genre, authors(artist), composer are all good.
# year recorded is not, and "audio channel" is non-existent.

# # song_properties = {
# #     "Album": audio.album,
# #     "Artist": audio.artist,
# #     "Title": audio.title,
# #     "Musical genre": audio.genre,
# #     "Authors": audio.albumartist,
# #     "Composer": audio.composer,
# #     "Year recorded": audio.year,
# # }
