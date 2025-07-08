from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>您好, 全世界!</h1>"

@app.route("/user/<name>")
def show_name(name):
    return f"<h1>您好, {escape(name)}</h1>"