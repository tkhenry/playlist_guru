import requests
import urllib
import base64

auth_url = "https://accounts.spotify.com/authorize"
client_id = ''
client_secret = ''
uri_red = 'http://127.0.0.1:5000/auth'
redirect_uri = {'redirect_uri':'http://127.0.0.1:5000/auth'}
token_url = 'https://accounts.spotify.com/api/token'
scope = 'playlist-read-private%20user-read-private'
response_type = 'code'

client_credentials = f'{client_id}:{client_secret}'
client_credentials = base64.b64encode(client_credentials.encode())


#get the user access code
def request_string():
    request_string = f'{auth_url}?client_id={client_id}&response_type={response_type}&scope={scope}&{urllib.parse.urlencode(redirect_uri)}'
    return request_string

#get all the other access codes
def get_tokens(code):
    token_data = {
        "grant_type": "authorization_code",
        "code": f"{code}",
        "redirect_uri": f"{uri_red}",
    }
    token_headers = {
        "Authorization": f"Basic {client_credentials.decode()}"
    }
    token_response = requests.post(token_url, data=token_data, headers=token_headers)
    return token_response.json()





