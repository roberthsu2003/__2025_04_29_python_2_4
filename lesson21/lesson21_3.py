from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>您好, 全世界!</h1>"