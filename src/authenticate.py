import requests
import urllib
import base64


auth_url = "https://accounts.spotify.com/authorize"
client_id = ''
client_secret = ''
redirect_uri = {'redirect_uri':'http://127.0.0.1:5000/auth'}
token_url = 'https://accounts.spotify.com/api/token'
scope = 'playlist-read-private'
response_type = 'code'

client_credentials = f'{client_id}:{client_secret}'
client_credentials = base64.b64encode(client_credentials.encode())


#get the request

request_string = f'{auth_url}?client_id={client_id}&response_type={response_type}&scope={scope}&{urllib.parse.urlencode(redirect_uri)}'
print(request_string)
#get_response = requests.get(request_string)



#Other token request data
token_data = {
    "grant_type" : "client_credentials"
}
token_headers = {
    "Authorization" : f"Basic {client_credentials.decode()}"
}

token_response = requests.post(token_url, data=token_data, headers = token_headers)
token_json = token_response.json()
access_token = token_json['access_token']
token_type = token_json['token_type']
token_expires = token_json['expires_in']
print("Token:",access_token, "Type:", token_type, "Expires In:", token_expires)





