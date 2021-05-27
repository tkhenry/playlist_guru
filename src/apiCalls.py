import authenticate
import requests
import main


def get_playlists(token_json):
    api_url = 'https://api.spotify.com/v1/me/playlists'
    '''
    :return: list of playlist objects for a specific user
    '''
    token_headers={
        "Authorization": f"Bearer {token_json['access_token']}",
    }
    playlist_json = requests.get(api_url, headers=token_headers).json()['items']
    playlist_dict = {playlist['name']:playlist['external_urls']['spotify'] for playlist in playlist_json}
    print(playlist_dict)
    return playlist_dict


def playlist_songs():
    pass