from turtle import title
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


def get_artist_id(artist):
    results = musicbrainzngs.search_artists(artist=artist, limit=5)
    for artist_info_set in results['artist-list']:
        if artist_info_set['name'].lower() == artist.lower():
            return artist_info_set['id']
        else:
            return "Not found"


def get_releases_by_artist(artist):
    titles_and_ids_dict = {}
    artist_id = get_artist_id(artist)
    releases = musicbrainzngs.browse_releases(
        artist=artist_id,
        # limit=30,
        # release_type=['album', 'single', 'ep',
        #               'compilation', 'soundtrack', 'live'],
        # release_status=['official']
        # release_type=musicbrainzngs.musicbrainz.VALID_RELEASE_TYPES,
        # release_status=musicbrainzngs.musicbrainz.VALID_RELEASE_STATUSES
    )
    for release in releases["release-list"]:
        titles_and_ids_dict[release["title"].lower()] = release["id"]
    return titles_and_ids_dict


def get_cover_art_with_musicbrainz(artist, album):
    # artist_id = get_artist_id(artist)
    album_id = get_releases_by_artist(artist)[album.lower()]
    return musicbrainzngs.get_image_list(releaseid=album_id)


#print(get_artist_id("Ben Folds"))
print(get_releases_by_artist("Ben Folds"))
print(get_cover_art_with_musicbrainz(
    artist="Ben Folds", album="Rockin' the Suburbs"))

# results = musicbrainzngs.get_artist_by_id(
#     id="51b7f46f-6c0f-46f2-9496-08c9ec2624d4", includes=["recordings", "releases", "works"])
# print(results)

# image_list = musicbrainzngs.get_image_list(
#     "7491bf54-68e7-452e-8b27-d9f73e085101")
# print(image_list)

# results = musicbrainzngs.search_artists(artist="ben folds")
# print(results)


# def find_cover_art(release_id):
#     data = musicbrainzngs.get_cover_art_list(
#         "46a48e90-819b-4bed-81fa-5ca8aa33fbf3")

#     for image in data["images"]:
#         if "Front" in image["types"] and image["approved"]:
#             print "It's is an approved front image!" % image["thumbnails"]["large"]
#             break
