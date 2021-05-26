from flask import Flask, request, redirect, url_for
import authenticate

app = Flask(__name__)

'''GLOBALS'''
user_code = ''
token_json = {}

@app.route('/auth')
def codes():
    global user_code
    global token_json
    #Gets the user authentication code from the url hash
    user_code = request.args.get('code', default='', type = str)
    token_json = authenticate.get_tokens(user_code)
    print(token_json)
    return redirect(url_for('home'))

@app.route('/')
def something():
    return redirect(authenticate.request_string())

@app.route('/home')
def home():
    return "You are home"



if __name__ == "__main__":
    app.run(debug=True)












