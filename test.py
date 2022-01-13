from song import Song
from m4a import M4ASong
from mp3 import MP3Song, pict_test

mp3_with_artwork = MP3Song(
    "/Users/mgermaine93/Desktop/test-music-folder/2-10 Granny.mp3")
mp3_without_artwork = MP3Song(
    "/Users/mgermaine93/Desktop/test-music-folder/03 Ragged Wood.mp3")
m4a_with_artwork = M4ASong(
    "/Users/mgermaine93/Desktop/test-music-folder/06 Domino.m4a")
m4a_without_artwork = M4ASong(
    "/Users/mgermaine93/Desktop/test-music-folder/06 Lonely Woman.m4a")

# MP3 with artwork testing
print("Testing an MP3 with artwork...")
print(mp3_with_artwork.is_file())
print(mp3_with_artwork.get_artist())
print(mp3_with_artwork.get_album())
print(mp3_with_artwork.create_search_term())
print(mp3_with_artwork.get_file_type())
print("############")
print(mp3_with_artwork.has_album_artwork())
print(mp3_with_artwork.pict_test())

# MP3 without artwork testing
print("Testing an MP3 without artwork...")
print(mp3_without_artwork.is_file())
print(mp3_without_artwork.get_artist())
print(mp3_without_artwork.get_album())
print(mp3_without_artwork.create_search_term())
print(mp3_without_artwork.get_file_type())
print("############")
print(mp3_without_artwork.has_album_artwork())
print(mp3_without_artwork.pict_test())


# M4A with artwork testing
print("Testing an M4A with artwork...")
print(m4a_with_artwork.is_file())
print(m4a_with_artwork.get_artist())
print(m4a_with_artwork.get_album())
print(m4a_with_artwork.create_search_term())
print(m4a_with_artwork.get_file_type())
print("############")
print(m4a_with_artwork.has_album_artwork())
print(m4a_with_artwork.pict_test())

# M4A without artwork testing
print("Testing an M4A without artwork...")
print(m4a_without_artwork.is_file())
print(m4a_without_artwork.get_artist())
print(m4a_without_artwork.get_album())
print(m4a_without_artwork.create_search_term())
print(m4a_without_artwork.get_file_type())
print("############")
print(m4a_without_artwork.has_album_artwork())
print(m4a_without_artwork.pict_test())
