from flask import Flask

app = Flask(__name__)

#defines starting point (root)
@app.route('/')

def hello_world():
    return 'Hello world'