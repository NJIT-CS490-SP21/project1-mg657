import requests
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, request
from spotify import get_artistID, song_info, lyricInfo, getSong
import random

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html") #Main page


@app.route("/result", methods=["POST", "GET"]) #If the user searches an Artist
def result():
    artist_id = get_artistID("artist")
    song_information = song_info(artist_id)
    return song_information

@app.route("/track", methods=["POST", "GET"]) #If the user wants a random song from a specific year
def track():
    song = getSong("track")
    return song

@app.route("/lucky", methods=["POST", "GET"]) #If the user wants a random song from my favorite artists
def lucky():
    artist_id = get_artistID("lucky")
    song_information = song_info(artist_id)
    return song_information

app.run(
    port=int(os.getenv("PORT", 8080)), 
    host=os.getenv("IP", "0.0.0.0"), 
    debug=True)