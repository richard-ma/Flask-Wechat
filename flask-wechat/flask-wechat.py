from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

@app.route('/echo')
def hello_world():
    return "echo"
