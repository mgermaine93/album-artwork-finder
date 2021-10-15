from project.classes.tune import Tune
from mutagen import File
from mutagen.id3 import ID3, APIC, error
from mutagen.mp3 import MP3
from pathlib import Path
from os import path


# What verbs/methods are specific to MP3s?
# detecting album artwork
# embedding album artwork


class MP3Tune(Tune):

    def __init__(self, file_path_to_song):
        self.file_path_to_song = file_path_to_song

    def detect_album_artwork(self):
        """
        Takes in a file path to a song and returns a boolean to determine whether or not the file already has album artwork associated with it.

        :param file_path_to_song:  a file path to an .mp3 or .m4a file.
        :type file_path_to_song: `string`, required.

        :return:  an object of type boolean that represents whether or not the song file passed into the function currently has album artwork associated with it.  `True` indicates that artwork is already associated with the song, whereas `False` indicates that artwork is not already associated with the song.
        :rtype:  `boolean`.
        """
        try:
            mp3 = MP3(file_path_to_song, ID3=ID3)
            tags = mp3.tags
            tags['covr']
            print("MP3 track has album artwork")
            return True
        except KeyError:
            print("MP3 track needs album artwork")
            return False

    def embed_album_artwork(self, file_path_to_image):
        """
        Takes in a file path to a song AND a file path to an image and saves the image as the album artwork to the song.

        :param file_path_to_song:  a file path to an .mp3 or .m4a file.
        :type file_path_to_song: `string`, required.
        :param file_path_to_image:  a file path to an image.
        :type file_path_to_image: `string`, required.

        :return:  an object of type boolean that represents whether or not the image was successfully saved as the album artwork to a song file.  `True` indicates that the image was successfully saved, whereas `False` indicates that the image was not successfully saved.
        :rtype:  `boolean`.
        """

        # Thanks to https://stackoverflow.com/questions/409949/how-do-you-embed-album-art-into-an-mp3-using-python
        mp3 = MP3(file_path_to_song, ID3=ID3)
        try:
            mp3.tags.add(
                APIC(
                    encoding=3,  # 3 is for utf-8
                    mime='image/jpg',  # image/jpeg or image/png
                    type=3,  # 3 is for the cover image
                    desc=u'Cover',
                    data=open(file_path_to_image, "rb").read()
                )
            )
            mp3.save()
            print("Artwork saved.")
            return True
        except Exception:
            print("Artwork was not added.")
            return False


mp3 = MP3Tune("/Users/mgermaine93/Desktop/Test-Music/Marvin Gaye & Tammi Terrell/20th Century Masters_ The Millennium Collection - The Best Of Marvin Gaye & Tammi Terrell/02 Ain't No Mountain High Enough.m4a")

# mp3.create_search_term()
# mp3.detect_album_artwork()
# mp3.embed_album_artwork()
