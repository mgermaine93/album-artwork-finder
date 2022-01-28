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


def get_artwork_through_last_fm(artist, album, api_key=API_KEY, api_secret=API_SECRET):

    network = pylast.LastFMNetwork(
        api_key=api_key,
        api_secret=api_secret,
    )

    album_data = network.get_album(artist, album)
    image = album_data.get_cover_image()
    return image


print(get_artwork_through_last_fm("Dave Matthews Band", "Crash"))
