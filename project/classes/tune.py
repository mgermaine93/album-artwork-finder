from tinytag import TinyTag
from os import path
from pathlib import Path


# What do I need to get from each song, REGARDLESS of file type?
# A determination as to whether or not it is a file.
# The file type.
# The search term that should be used to retrieve the album artwork.

class Tune():

    def __init__(self, file_path_to_song):
        self.file_path_to_song = file_path_to_song

    def is_file(self):
        if path.isfile(self.file_path_to_song):
            print("Yep, it's a file.")
            return True
        else:
            print("Nope, not a file.")
            return False

    def get_artist(self):
        return TinyTag.get(self.file_path_to_song).artist

    def get_album(self):
        return TinyTag.get(self.file_path_to_song).album

    def create_search_term(self):
        """
        Takes in a file path to a song and returns a phrase that will be used to search for the song's corresponding album artwork.

        :param file_path_to_song:  a file path to an .mp3 or .m4a file.
        :type file_path_to_song: `string`, required.

        :return:  an object of type string that represents the search term to be used when finding album artwork for song file passed into the function.
        :rtype:  `string`.
        """
        artist = self.get_artist()
        album = self.get_album()
        term = f"{artist} {album} Album Cover"
        return term

    def get_file_type(self):
        file_type = Path(self.file_path_to_song).suffix
        return file_type


song = Tune("/Users/mgermaine93/Desktop/Test-Music/Marvin Gaye & Tammi Terrell/20th Century Masters_ The Millennium Collection - The Best Of Marvin Gaye & Tammi Terrell/02 Ain't No Mountain High Enough.m4a")

# print(song.is_file())
# print(song.create_search_term())
# print(song.get_file_type())


# # song.is_file()

# print(TinyTag.get("/Users/mgermaine93/Desktop/Test-Music/Marvin Gaye & Tammi Terrell/20th Century Masters_ The Millennium Collection - The Best Of Marvin Gaye & Tammi Terrell/02 Ain't No Mountain High Enough.m4a"))
