# This is where all of the logic comes together for now.

from project.helpers import create_search_term, detect_album_artwork, embed_album_artwork
from project.artwork_grabber import get_album_artwork
import os
from pathlib import Path
from project.classes.song import Tune
from project.classes.mp3 import MP3Tune
from project.classes.m4a import M4ATune


# file_path_to_music_library = "/Users/mgermaine93/Desktop/Test-Music"
file_path_to_music_library = "/Users/mgermaine93/Desktop/Test-Music/"
file_path_to_songs = "/Users/mgermaine93/Desktop/Test-Music"
save_folder = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork"

# iTunes Media is stored ARIST > ALBUM > SONG

# https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory

# returns a list of filepaths to songs


def find_music(file_path_to_music_library):
    song_collection = []
    for subdir, dirs, files in os.walk(file_path_to_music_library):
        for file in files:
            # print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".mp3") or filepath.endswith(".m4a"):
                # print(filepath)
                song_collection.append(filepath)
    return song_collection


def main_run_file(songs):
    for file in range(len(songs)):
        # need to check the save_folder to see if artwork image is already there
        song = Tune(songs[file])
        search_term = song.create_search_term()
        image = f"{save_folder}{search_term}_new_artwork.jpeg"

        if song.get_file_type() == ".m4a":
            song = M4ATune(songs[file])
            # if the file doesn't have album artwork
            if not song.has_album_artwork():
                # if the artwork is already saved
                if Path(image).is_file():
                    # simply embed the artwork
                    song.embed_album_artwork(image)
                else:
                    # otherwise, retrieve the artwork and save it to the file
                    image = get_album_artwork(search_term, save_folder)
                    song.embed_album_artwork(image)
            else:
                print("Song already has artwork")
                continue

        elif song.get_file_type() == ".mp3":
            song = MP3Tune(songs[file])
            # if the file doesn't have album artwork
            if not song.has_album_artwork():
                # if the artwork is already saved
                if Path(image).is_file():
                    # simply embed the artwork
                    song.embed_album_artwork(image)
                else:
                    # otherwise, retrieve the artwork and save it to the file
                    image = get_album_artwork(search_term, save_folder)
                    song.embed_album_artwork(image)
            else:
                print("Song already has artwork")
                continue

        else:
            print("Song is not a valid file type")
            pass

        print("Done")


songs = songs = find_music(file_path_to_music_library)
main_run_file(songs)

# checks the saved artwork folder to see if artwork already exists

# pass
# def get_artists(file_path):
#     artists = [
#         artist for artist in Path(file_path).iterdir() if os.path.isdir(artist)
#     ]
#     print(artists[0])

# def get_albums(file_path):
#     albums = [
#         album for album in Path(file_path).iterdir() if os.path.isdir(album)
#     ]
#     print(albums[0])

# def get_songs(file_path):
#     songs = [
#         song for song in Path(file_path).iterdir() if os.path.isfile(song)
#     ]
#     print(songs[0])

# get_songs(file_path_to_music_library)
#     for artist in artists:
#         artist_path = os.path.join(file_path_to_music_library, artist)
#         print(artist_path)

# def run_program(file_path_to_music_library):
#     if os.path.isdir(file_path_to_music_library):
#         with os.scandir(file_path_to_music_library) as music_library:

#     else:
#         print("Not a real directory!")
#         return False

# def get_artist_paths(file_path_to_music_library):
#     artist_paths = [
#         artist for artist in Path(file_path_to_music_library).iterdir()
#     ]
#     for artist in artist_paths:
#         artist_path = os.path.join(file_path_to_music_library, artist)
#         print(artist_path)

#     artists = [
#         # if not artist.name.startswith(".")
#         artist for artist in Path(file_path_to_music_library).iterdir()
#     ]
#     for artist in artists:
#         artist_path = os.path.join(file_path_to_music_library, artist)
#         print(f"Artist path is here: {artist_path}")

#     if os.path.isdir(artist_path):
#         pass

#     albums = [
#         album for album in Path(artist_path).iterdir() if not album.name.startswith(".")
#     ]

#     for album in albums:
#         album_path = os.path.join(artist_path, album)

#     if os.path.isdir(album_path):
#         pass

# songs = [
#     song for song in Path(album_path).iterdir() if not song.name.startswith(".")
# ]

# for song in songs:
#     song_path = os.path.join(album_path, song)

# if os.path.isfile(song_path):
#     pass

# file_type = Path(song_path).suffix.lower()

# # actual function call is here
# get_artist_paths(file_path_to_music_library)

# with os.scandir(file_path_to_music_library) as music_library:
#     # artists
#     artists = [
#         # if not artist.name.startswith(".")
#         artist for artist in Path(file_path_to_music_library).iterdir()
#     ]
#     for artist in artists:
#         artist_path = os.path.join(file_path_to_music_library, artist)
#         print(f"Artist path is here: {artist_path}")

#         if os.path.isdir(artist_path):
#             # albums
#             albums = [
#                 album for album in Path(artist_path).iterdir() if not album.name.startswith(".")
#             ]

#             for album in albums:
#                 album_path = os.path.join(artist_path, album)

#                 if os.path.isdir(album_path):
#                     print(f"    Album path is here: {album_path}")
#                     # songs
#                     songs = [
#                         song for song in Path(album_path).iterdir() if not song.name.startswith(".")
#                     ]

#                     for song in songs:
#                         song_path = os.path.join(album_path, song)

#                         if os.path.isfile(song_path):
#                             print(f"        Song path is here: {song_path}")

#                             file_type = Path(song_path).suffix.lower()
#                             if (file_type == ".m4a" or file_type == ".mp3") and Path(song_path).is_file():
#                                 search_term = create_search_term(song_path)

#                                 if not detect_album_artwork(song_path):
#                                     file_path_to_artwork = get_album_artwork(
#                                         search_term, save_folder)
#                                     embed_album_artwork(
#                                         song_path, file_path_to_artwork)
#                                     print(
#                                         f"Artwork should be saved for {song_path}")
#                                     count += 1
#                                 else:
#                                     continue
#                             else:
#                                 print(
#                                     f"            Song path {song_path} is not M4A or MP3.")
#                                 continue
#                         else:
#                             print(f"{song_path} is not a valid file.")
#                 else:
#                     print(f"{album_path} is not a valid directory.")
#                     continue

#         else:
#             print(f"{artist_path} is not a valid directory.")
#             continue

# print(f"{count} should be 10.")
# print("Success, I think.")

# # with os.scandir(file_path_to_songs) as songs:

# #     count = 0

# #     # this currently works for a single directory of tracks, e.g., an album.
# #     # will need to update so that it works for directories containing other directories, e.g., other albums AS WELL AS stand-alone tracks.
# #     for song in songs:
# #         file_type = Path(song).suffix.lower()
# #         if (file_type == ".m4a" or file_type == ".mp3") and song.is_file():

# #             search_term = create_search_term(song.path)

# #             if not detect_album_artwork(song):
# #                 file_path_to_artwork = get_album_artwork(
# #                     search_term, save_folder)
# #                 embed_album_artwork(song, file_path_to_artwork)
# #                 count += 1
# #             else:
# #                 print("Something done messed up...")
# #                 continue

# #     print(f"{count} should be 10.")

# # print("Success, I think.")
