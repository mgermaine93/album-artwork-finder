import os
import pylast
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("SHARED_SECRET")
USER_AGENT = os.getenv("USER_AGENT")
# HEADERS is requested in the Last FM documentation, but isn't an accepted parameter in pyLast...
# HEADERS = {
#     "user-agent": USER_AGENT
# }


def get_artwork_with_last_fm(artist, album, api_key=API_KEY, api_secret=API_SECRET):
    """
    Returns a link to the EXTRA LARGE image size.  Other sizes can be SIZE_LARGE, SIZE_MEDIUM, or SIZE_SMALL
    """
    network = pylast.LastFMNetwork(
        api_key=api_key,
        api_secret=api_secret,
    )

    album_data = network.get_album(artist, album)
    image_url = album_data.get_cover_image()
    return image_url


# print(get_artwork_through_last_fm(artist="Sylvan Esso", album="Sylvan Esso"))
