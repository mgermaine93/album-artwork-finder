from helpers import create_search_term, detect_album_artwork, embed_album_artwork
from artwork_grabber import get_album_artwork

song = "/Users/mgermaine93/Desktop/01 Up All Night.m4a"
save_folder = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork"

search_term = create_search_term(song)

if not detect_album_artwork(song):
    file_path_to_artwork = get_album_artwork(search_term, save_folder)
    embed_album_artwork(song, file_path_to_artwork)
else:
    print("Something done messed up...")
