from flask import Flask, request, redirect, url_for
import authenticate

app = Flask(__name__)

'''GLOBALS'''
user_code = ''



@app.route('/auth')
def codes():
    global user_code
    user_code = request.args.get('code', default='', type = str)
    return redirect(url_for('home'))


@app.route('/')
def something():
    return "Hello World"

@app.route('/home')
def home():
    print(user_code)
    return "You are home"



if __name__ == "__main__":
    app.run(debug=True)












