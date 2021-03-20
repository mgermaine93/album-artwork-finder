# Playing around with TinyTag

from tinytag import TinyTag

mp3_file_name = "/Users/mgermaine93/Desktop/Test-Music/03 Dylan Thomas.mp3"
m4a_file_name = "/Users/mgermaine93/Desktop/Test-Music/03 Dylan Thomas.m4a"
album_art = "/Users/mgermaine93/Desktop/better oblivion community center.jpg"

tag = TinyTag.get(mp3_file_name, image=True)
image_data = tag.get_image()
print(image_data)  # This prints "None"

tag2 = TinyTag.get(m4a_file_name, image=True)
image_data_2 = tag.get_image()
print(image_data_2)  # This also prints "None"
