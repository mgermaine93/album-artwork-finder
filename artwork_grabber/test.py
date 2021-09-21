# This is where all of the logic comes together for now.

from helpers import create_search_term, detect_album_artwork, embed_album_artwork
from artwork_grabber import get_album_artwork
import os
from pathlib import Path


file_path_to_songs = "/Users/mgermaine93/Desktop/Test-Music"
save_folder = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork"

with os.scandir(file_path_to_songs) as songs:
    for song in songs:
        file_type = Path(song).suffix.lower()
        if (file_type == ".m4a" or file_type == ".mp3") and song.is_file():

            count = 0

            search_term = create_search_term(song.path)

            if not detect_album_artwork(song):
                file_path_to_artwork = get_album_artwork(
                    search_term, save_folder)
                embed_album_artwork(song, file_path_to_artwork)
                count += 1
            else:
                print("Something done messed up...")

            print(f"{count} should be 14.")

print("Success, I think.")
