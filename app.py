import flask
app = flask.Flask(__name__)

@app.route('/')
def home():
    return """
<center> 
    <img src="https://i.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.webp" style="border-radius: 12px;"/> 
</center> 
<style>
    body { 
        background: antiquewhite;
    }
</style>"""
from flask import Flask
app = Flask(name)

@app.route('/')
def hello_world():
    return 'GreyMatters'


if name == "main":
    app.run()
