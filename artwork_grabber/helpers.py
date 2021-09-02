from mutagen.mp4 import MP4, MP4Cover
from mutagen import File
from mutagen.id3 import ID3, APIC, error
from mutagen.mp3 import MP3
from pathlib import Path


def create_search_term(song):
    """
    Takes in a file path to a song (string) and returns a phrase that will be used to search for the song's corresponding album artwork (string). 
    """

    album = song.Song.get_album(song)
    artist = song.Song.get_artist(song)
    term = f"{artist} {album} album cover"
    print(f"Output of get_search_term() function: {term}")
    return term


def detect_album_artwork(song):
    """
    Takes in a file path to a song (string) and returns a boolean to determine whether or not the file already has album artwork associated with it.
    """

    file_type = Path(song.file_path_to_song).suffix.lower()

    if file_type == ".m4a":
        try:
            m4a = MP4(song)
            tags = m4a.tags
            tags['covr']
            return True
        except KeyError:
            print("M4A track needs album artwork")
            return False

    elif file_type == ".mp3":
        try:
            mp3 = MP3(song, ID3=ID3)
            tags = mp3.tags
            tags['covr']
            return True
        except KeyError:
            print("MP3 track needs album artwork")
            return False

    else:
        print("Filename name is not M4A nor MP3")
        return False


def embed_album_artwork(song, album_art):
    """
    Takes in a file path to a song (string) and a file path to an image (string) and saves the image as the album artwork to the song.
    """

    file_type = Path(song.file_path_to_song).suffix.lower()

    print(file_type)
    if file_type == ".m4a":
        m4a = MP4(song.file_path_to_song)

        # Thanks to: https://stackoverflow.com/questions/37897801/embedding-album-cover-in-mp4-file-using-mutagen
        with open(album_art, "rb") as f:
            m4a.tags["covr"] = [
                MP4Cover(f.read(), imageformat=MP4Cover.FORMAT_JPEG)
            ]
            m4a.save()
            print("artwork saved")

    elif file_type == ".mp3":
        # Thanks to https://stackoverflow.com/questions/409949/how-do-you-embed-album-art-into-an-mp3-using-python
        mp3 = MP3(song.file_path_to_song, ID3=ID3)
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
    else:
        print("Filename name is not M4A nor MP3")
