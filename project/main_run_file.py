# This is where all of the logic comes together for now.

from project.helpers import create_search_term, detect_album_artwork, embed_album_artwork
from project.artwork_grabber import get_album_artwork
import os
from pathlib import Path

file_path_to_music_library = "/Users/mgermaine93/Desktop/Test-Music"
file_path_to_songs = "/Users/mgermaine93/Desktop/Test-Music"
save_folder = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork"

# iTunes Media is stored ARIST > ALBUM > SONG

count = 0

with os.scandir(file_path_to_music_library) as music_library:
    # artists
    artists = [
        # if not artist.name.startswith(".")
        artist for artist in Path(file_path_to_music_library).iterdir()
    ]
    for artist in artists:
        artist_path = os.path.join(file_path_to_music_library, artist)
        print(f"Artist path is here: {artist_path}")

        if os.path.isdir(artist_path):
            albums = [
                album for album in Path(artist_path).iterdir() if not album.name.startswith(".")
            ]

            for album in albums:
                album_path = os.path.join(artist_path, album)

                if os.path.isdir(album_path):
                    print(f"    Album path is here: {album_path}")
                    songs = [
                        song for song in Path(album_path).iterdir() if not song.name.startswith(".")
                    ]

                    for song in songs:
                        song_path = os.path.join(album_path, song)

                        if os.path.isfile(song_path):
                            print(f"        Song path is here: {song_path}")

                            file_type = Path(song_path).suffix.lower()
                            if (file_type == ".m4a" or file_type == ".mp3") and Path(song_path).is_file():
                                search_term = create_search_term(song_path)

                                if not detect_album_artwork(song_path):
                                    file_path_to_artwork = get_album_artwork(
                                        search_term, save_folder)
                                    embed_album_artwork(
                                        song_path, file_path_to_artwork)
                                    print(
                                        f"Artwork should be saved for {song_path}")
                                    count += 1
                                else:
                                    continue
                            else:
                                print(
                                    f"            Song path {song_path} is not M4A or MP3.")
                                continue
                        else:
                            print(f"{song_path} is not a valid file.")
                else:
                    print(f"{album_path} is not a valid directory.")
                    continue

        else:
            print(f"{artist_path} is not a valid directory.")
            continue

print(f"{count} should be 10.")
print("Success, I think.")

# with os.scandir(file_path_to_songs) as songs:

#     count = 0

#     # this currently works for a single directory of tracks, e.g., an album.
#     # will need to update so that it works for directories containing other directories, e.g., other albums AS WELL AS stand-alone tracks.
#     for song in songs:
#         file_type = Path(song).suffix.lower()
#         if (file_type == ".m4a" or file_type == ".mp3") and song.is_file():

#             search_term = create_search_term(song.path)

#             if not detect_album_artwork(song):
#                 file_path_to_artwork = get_album_artwork(
#                     search_term, save_folder)
#                 embed_album_artwork(song, file_path_to_artwork)
#                 count += 1
#             else:
#                 print("Something done messed up...")
#                 continue

#     print(f"{count} should be 10.")

# print("Success, I think.")
