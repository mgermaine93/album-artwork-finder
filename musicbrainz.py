from turtle import title
import musicbrainzngs
import os
from dotenv import load_dotenv

# https://python-musicbrainzngs.readthedocs.io/en/v0.7.1/api/?highlight=browse_artists#cover-art
# https://python-musicbrainzngs.readthedocs.io/en/v0.7.1/usage/#more-examples

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
    """Retrieves an artist's unique identifier from the Musicbrainz database.

    Args:
        artist (str) : the artist (singer, band, soloist, etc.) for which you would like to retrieve data from.

    Returns:
        artist_id (str) : the unique id that corresponds to the artist, if found in the Musicbrainz database.
        (If no idea is found, then the boolean value "False" is returned)
    """
    results = musicbrainzngs.search_artists(artist=artist, limit=5)
    for artist_info_set in results['artist-list']:
        if artist_info_set['name'].lower() == artist.lower():
            artist_id = artist_info_set['id']
            return artist_id
        else:
            return False


def has_musicbrainz_artwork(album_data):
    """Determines whether or not an album has artwork in the Musicbrainz database.

    Args:
        album_data (dict/json) : a dict containing information about an album as it is returned from the Musicbrainz database.

    Returns:
        "True" if an album has album artwork in the Musicbrainz database.
        "False" if an album does not have album artwork in the Musicbrainz database.
    """
    if album_data["cover-art-archive"]["front"] == "true":
        return True
    else:
        return False


def get_releases_with_artwork_by_artist(artist):
    """
    Docstring needed.
    """
    titles_and_ids_dict = {}
    releases = musicbrainzngs.browse_releases(
        artist=get_artist_id(artist),
        # limit=30,
        # release_type=['album', 'single', 'ep',
        #               'compilation', 'soundtrack', 'live'],
        # release_status=['official']
        # release_type=musicbrainzngs.musicbrainz.VALID_RELEASE_TYPES,
        # release_status=musicbrainzngs.musicbrainz.VALID_RELEASE_STATUSES
    )
    for release in releases["release-list"]:
        if has_musicbrainz_artwork(release):
            titles_and_ids_dict[release["title"].lower()] = release["id"]
    if titles_and_ids_dict:
        return titles_and_ids_dict
    else:
        return False


def get_artwork_with_musicbrainz(artist, album):
    """
    Returns the binary image data of the frontal cover image of an album in the form of a str.
    """
    try:
        album_id = get_releases_with_artwork_by_artist(artist)[album.lower()]
        print(album_id)
    except KeyError:
        return f"{album} by {artist} was not available in the musicbrainz database."
    # returns binary... not the best?
    # return musicbrainzngs.get_image_front(releaseid=album_id)
    # THIS below returns a url to the image, which I think I prefer
    image_url = musicbrainzngs.get_image_list(releaseid=album_id)[
        "images"][0]["image"]
    return image_url


# print(get_artwork_with_musicbrainz("John Coltrane", "Giant Steps"))
# /Users/mgermaine93/Desktop/test-music-folder/01 Giant Steps.m4a
