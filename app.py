from flask import Flask

app=Flask(__name__)


@app.route('/')
def home():
    return "Hello world"

@app.route('/')
def about():
    return "this is about this page"