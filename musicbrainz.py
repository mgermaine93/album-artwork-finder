import musicbrainzngs
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("PERSONAL_EMAIL")
# API_SECRET = os.getenv("SHARED_SECRET")
# USER_AGENT = os.getenv("USER_AGENT")

user_agent = musicbrainzngs.set_useragent(
    app="Matt's Album Artwork Grabber",
    version="1.0.0",
    contact="mgermaine93@gmail.com"
)

# results = musicbrainzngs.get_artist_by_id(
#     id="51b7f46f-6c0f-46f2-9496-08c9ec2624d4", includes=["recordings", "releases", "works"])
# print(results)

image_list = musicbrainzngs.get_image_list(
    "7491bf54-68e7-452e-8b27-d9f73e085101")
print(image_list)

# results = musicbrainzngs.search_artists(artist="ben folds")
# print(results)


# def find_cover_art(release_id):
#     data = musicbrainzngs.get_cover_art_list(
#         "46a48e90-819b-4bed-81fa-5ca8aa33fbf3")

#     for image in data["images"]:
#         if "Front" in image["types"] and image["approved"]:
#             print "It's is an approved front image!" % image["thumbnails"]["large"]
#             break
