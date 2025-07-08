from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>您好, 全世界!</h1>"

@app.route("/name")
def name():
    return "<h1>您好, 這是name的頁面!</h1>"