from project.classes.tune import Tune
from mutagen.mp4 import MP4, MP4Cover

# What verbs/methods are specific to M4As?
# detecting album artwork
# embedding album artwork


class M4ATune(Tune):

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
            m4a = MP4(self.file_path_to_song)
            tags = m4a.tags
            print(tags)
            tags['covr']
            print("M4a track has album artwork")
            return True
        except KeyError:
            print("M4A track needs album artwork")
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

        m4a = MP4(file_path_to_song)

        # Thanks to: https://stackoverflow.com/questions/37897801/embedding-album-cover-in-mp4-file-using-mutagen
        try:
            with open(file_path_to_image, "rb") as f:
                m4a.tags["covr"] = [
                    MP4Cover(f.read(), imageformat=MP4Cover.FORMAT_JPEG)
                ]
                m4a.save()
                print("Artwork saved")
                return True
        except Exception:
            print("Artwork was not added.")
            return False


m4a = M4ATune(
    "/Users/mgermaine93/Downloads/Phoebe Bridgers - Punisher/Phoebe Bridgers - Punisher - 06 Chinese Satellite.mp3")

# m4a.create_search_term()
# m4a.detect_album_artwork()
# m4a.embed_album_artwork()
