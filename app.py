import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/")

def page():
    text = '''<!DOCTYPE html>
        <html>
        <head>
        <title></title>
        <link rel="stylesheet" href="{{ url_for('static', filename='home.css') }}">
        </head>
        <body>
        <h2>Take a break.</h2>
        <p align="center"><a href=begin ><button class=grey style="height:75px;width:150px">begin.</button></a></p>
        </body>
        </html>'''
    return text

def index():
    length = input("length: ")
    if length == 'short':
        size = 264
    animal = "your mom"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="write a short story about a " + animal,
        temperature=0.7,
        max_tokens=size,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    return response["choices"][0]["text"][:response["choices"][0]["text"].rfind('.')+1]

def create():
    f = open('C:\Users\charl\OneDrive\Documents\flask\openai-quickstart-python-master\templates\p1.html', 'w')
    f.write(index[:index().find('.')])
    return f

@app.route('/begin')
def begin():
    return render_template(create())