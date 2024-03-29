from musicbrainz import get_artwork_with_musicbrainz
from last_fm import get_artwork_with_last_fm
from song import Song
from m4a import M4ASong
from mp3 import MP3Song
from musicbrainzngs import get_image_list

# https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests

print(get_artwork_with_musicbrainz("John Coltrane", "Giant Steps"))


# mp3_without_artwork = MP3Song(
#     "/Users/mgermaine93/Desktop/test-music-folder/08 Basic Space.mp3")

# mp3_without_artwork.embed_album_url_artwork(
#     "https://lastfm.freetls.fastly.net/i/u/300x300/45ee0a97add34e34ce3cccaa16feec9f.jpg")

# if not mp3_without_artwork.has_album_artwork():
#     if get_artwork_with_last_fm(artist=mp3_without_artwork.get_artist(), album=mp3_without_artwork.get_album()):
#         artwork_url = get_artwork_with_last_fm(
#             artist=mp3_without_artwork.get_artist(), album=mp3_without_artwork.get_album())
#         mp3_without_artwork.embed_album_artwork(artwork_url)
#         print("Embedded URL artwork!")
#     elif get_artwork_with_musicbrainz(artist=mp3_without_artwork.get_artist(), album=mp3_without_artwork.get_album()):
#         artwork_binary_file = get_artwork_with_musicbrainz(
#             artist=mp3_without_artwork.get_artist(), album=mp3_without_artwork.get_album())
#         mp3_without_artwork.embed_album_binary(
#             binary_to_artwork=artwork_binary_file)
#         print("Embedded binary artwork!")
# print("Success!")


# # TEST FILE (used to test/print out output of different functions, etc.)


# mp3_with_artwork = MP3Song(
#     "/Users/mgermaine93/Desktop/test-music-folder/2-10 Granny.mp3")
# mp3_without_artwork = MP3Song(
#     "/Users/mgermaine93/Desktop/test-music-folder/03 Ragged Wood.mp3")
# m4a_with_artwork = M4ASong(
#     "/Users/mgermaine93/Desktop/test-music-folder/06 Domino.m4a")
# m4a_without_artwork = M4ASong(
#     "/Users/mgermaine93/Desktop/test-music-folder/06 Lonely Woman.m4a")

# # # MP3 with artwork testing
# # print("Testing an MP3 with artwork...")
# # # print(mp3_with_artwork.is_file())
# # # print(mp3_with_artwork.get_artist())
# # # print(mp3_with_artwork.get_album())
# # print(mp3_with_artwork.create_search_term())
# # print(mp3_with_artwork.get_file_type())
# # print("############")
# # print(f"Has Album Artwork Results: {mp3_with_artwork.has_album_artwork()}")
# # # print(f"Pict Test Results: {mp3_with_artwork.pict_test()}")
# # print("############")


# # # MP3 without artwork testing
# # print("Testing an MP3 without artwork...")
# # # print(mp3_without_artwork.is_file())
# # # print(mp3_without_artwork.get_artist())
# # # print(mp3_without_artwork.get_album())
# # print(mp3_without_artwork.create_search_term())
# # print(mp3_without_artwork.get_file_type())
# # print("############")
# # print(f"Has Album Artwork Results: {mp3_without_artwork.has_album_artwork()}")
# # # print(f"Pict Test Results: {mp3_without_artwork.pict_test()}")
# # print("############")


# # M4A with artwork testing
# print("Testing an M4A with artwork...")
# # print(m4a_with_artwork.is_file())
# # print(m4a_with_artwork.get_artist())
# # print(m4a_with_artwork.get_album())
# print(m4a_with_artwork.create_search_term())
# print("############")
# print(m4a_with_artwork.has_album_artwork())
# # print(m4a_with_artwork.pict_test())
# print("############")


# # M4A without artwork testing
# print("Testing an M4A without artwork...")
# # print(m4a_without_artwork.is_file())
# # print(m4a_without_artwork.get_artist())
# # print(m4a_without_artwork.get_album())
# print(m4a_without_artwork.create_search_term())
# print("############")
# print(m4a_without_artwork.has_album_artwork())
# # print(m4a_without_artwork.pict_test())
