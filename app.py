from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world!"

@app.route('/shri')
def shri():
    return "Hi Shri, you're awesome!"

app.run(port=5000)