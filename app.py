import os

import openai
from flask import Flask, redirect, render_template, request, url_for
import requests

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/")

def index():
    length = input("length: ")
    if length == 'short':
        size = 264
    animal = input("favourite animal: ")
    mood = input('how are you feeling? ')
    if mood == 'sad':
        mood = 'happy'
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="write" + mood + " a short story about a " + animal,
        temperature=0.7,
        max_tokens=size,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    story = response["choices"][0]["text"][:response["choices"][0]["text"].rfind('.')+1]
    return story