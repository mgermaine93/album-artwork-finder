from tinytag import TinyTag


class Song:
    def __init__(self, file_path_to_song):
        self.file_path_to_song = file_path_to_song

    def print_file_path(self):
        print(self.file_path_to_song)

    def get_album(self):
        # return TinyTag.get(self.file_path_to_song).album
        print(TinyTag.get(self.file_path_to_song).album)

    def get_album_artist(self):
        return TinyTag.get(self.file_path_to_song).albumartist

    def get_artist(self):
        return TinyTag.get(self.file_path_to_song).artist

    def get_audio_offset(self):
        return TinyTag.get(self.file_path_to_song).audio_offset

    def get_bitrate(self):
        return TinyTag.get(self.file_path_to_song).bitrate

    def get_comment(self):
        return TinyTag.get(self.file_path_to_song).comment

    def get_composer(self):
        return TinyTag.get(self.file_path_to_song).composer

    def get_disc(self):
        return TinyTag.get(self.file_path_to_song).disc

    def get_disc_total(self):
        return TinyTag.get(self.file_path_to_song).disc_total

    def get_disc_total(self):
        return TinyTag.get(self.file_path_to_song).disc_total

    def get_duration(self):
        return TinyTag.get(self.file_path_to_song).duration

    def get_filesize(self):
        return TinyTag.get(self.file_path_to_song).filesize

    def get_genre(self):
        return TinyTag.get(self.file_path_to_song).genre

    def get_samplerate(self):
        return TinyTag.get(self.file_path_to_song).samplerate

    def get_title(self):
        return TinyTag.get(self.file_path_to_song).title

    def get_track(self):
        return TinyTag.get(self.file_path_to_song).track

    def get_track_total(self):
        return TinyTag.get(self.file_path_to_song).track_total

    def get_year(self):
        return TinyTag.get(self.file_path_to_song).year


song = Song('/Users/mgermaine93/Desktop/02 Shoot To Thrill.m4a')
song.print_file_path()
song.get_album()

tag = TinyTag.get('/Users/mgermaine93/Desktop/02 Shoot To Thrill.m4a')
print(tag.album)
# print(song.get_album)
# print(song.get_artist)
# tag = TinyTag.get('/some/music.mp3', image=True)
# image_data = tag.get_image()
