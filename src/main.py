from flask import Flask, request, redirect, url_for, render_template
import authenticate
import apiCalls as api
from templates import *

app = Flask(__name__)

'''GLOBALS'''
user_code = ''
token_json = {}

def get_token_json():
    return token_json

@app.route('/auth')
def codes():
    global user_code
    global token_json
    #Gets the user authentication code from the url hash
    user_code = request.args.get('code', default='', type = str)
    token_json = authenticate.get_tokens(user_code)
    return redirect(url_for('home'))

@app.route('/')
def spotify_auth():
    return redirect(authenticate.request_string())

@app.route('/home')
def home():
    playlist_dict = api.get_playlists(token_json)
    return render_template("homepage.html", data=playlist_dict)

if __name__ == "__main__":
    app.run(debug=True)












