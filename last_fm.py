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


print(get_artwork_through_last_fm("Bill Evans", "For Lovers"))

# payload = {
#     "api_key": API_KEY,
#     "method": "auth.getToken",
#     "format": "json"
# }

# # Fetches a request token
# token_response = requests.get(
#     "https://ws.audioscrobbler.com/2.0/", headers=headers, params=payload)
# print(token_response.status_code)

# # request_token = token_response.json()["token"]

# # Requests authorization from the user -- will probably open a browser
# authorization_url = f"http://www.last.fm/api/auth/?api_key={API_KEY}&token={request_token}"
# authorization_response = requests.get(authorization_url, headers=headers)

# # Constructs the API signature
# api_signature = md5(
#     f"api_key{API_KEY}methodauth.getSessiontoken{request_token}{SHARED_SECRET}".encode('utf-8')).hexdigest()

# # Fetches the web service session
# web_service_session_url = f'http://ws.audioscrobbler.com/2.0/?api_key={API_KEY}&token={request_token}&api_sig={api_signature}&method=auth.getSession&format=json'
# web_service_response = requests.get(
#     web_service_session_url, headers=headers).json()
# # print(web_service_response)


# # api_signature = md5("api_key={API_KEY}")
# # # stuff = f'http://ws.audioscrobbler.com/2.0/?method=auth.getToken&api_key={API_KEY}&format=json'
# # new_stuff = f'http://ws.audioscrobbler.com/2.0/?api_key={API_KEY}&method=auth.getToken&auth.getSession&format=json'


# # print(os.getenv("PATH"))
# # print(os.getenv("API_KEY"))
