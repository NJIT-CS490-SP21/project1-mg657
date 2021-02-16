import requests
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, request
import random

app = Flask(__name__)
load_dotenv(find_dotenv()) # Load API keys from .env
AUTH_URL = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(
    AUTH_URL,
    {
        "grant_type": "client_credentials",
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
    }
)
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token'] # Save access token
headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
params={ 'market': 'US'} # Specify market parameter

def get_artistID(endpoint):
    if endpoint == "result":
        artist = request.form['Artist']
        if (len(artist) ==0):
            artist = 'Logic'
        headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
        params_genius={ 'q': artist, 
        'type': 'track,artist'} # Specify  parameter 
        req_artist = requests.get('https://api.spotify.com/v1/search', 
        headers=headers,
        params=params_genius).json() 
        if (len(req_artist['artists']['items'])==0):
            artist_id = '4xRYI6VqpkE3UwrDrAZL8L'
        else:
            artist_id = req_artist['artists']['items'][0]['id']
    else:
        artist_list = [
        "3TVXtAsR1Inumwj472S9r4", #Drake
        "06HL4z0CvFAxyc27GXpf02", #Taylor Swift   
        "66CXWjxzNUsdJxJ2JdwvnR", #Ariana Grande
        "4xRYI6VqpkE3UwrDrAZL8L", #Logic
        "4MCBfE4596Uoi2O4DtmEMz", #Juice Wrld
        "1RyvyyTE3xzB2ZywiAwp0i", #Future
        "07YZf4WDAMNwqr4jfgOZ8y", #Jason Derulo
        "0C8ZW7ezQVs4URX5aX7Kqx", #Selena Gomez
        ]
        rand_Artist = random.randint(0,7) #picks random artist from list with index 0-7
        artist_id = artist_list[rand_Artist]
    return artist_id
def song_info(artist_id):
    params_spotify={ 'market': 'US'} # Specify market parameter
    req = requests.get(
            'https://api.spotify.com/v1/artists/'+artist_id+'/top-tracks', headers=headers, params=params_spotify).json() 
    rand_song = random.randint(0, len(req["tracks"]) - 1)  # Picks random song from all the songs by certain artist
    artist_name_list=req['tracks'][rand_song]['artists']
    song_name=req['tracks'][rand_song]['name']
    song_image=req['tracks'][rand_song]['album']['images'][1]['url']
    song_prev_link=req['tracks'][rand_song]['preview_url']
    song_link=req['tracks'][rand_song]['external_urls']['spotify']
    artist_name = []
    for key in artist_name_list:  # For each item in list of artists
        artist_name.append(key["name"])  # Add the artist to the list
    return render_template(  # Send all info to html page
        'result.html',
        artist_name=artist_name,
        song_name=song_name,
        song_image=song_image,
        song_prev_link=song_prev_link,
        song_link=song_link,
        song_lyrics = lyricInfo(song_name),
        len = len(artist_name)
        )
def lyricInfo(song_name):
    base_url_genius = "http://api.genius.com"
    headers_genius = {'Authorization': 'Bearer ' + os.getenv("GENIUS_ACCESS_TOKEN")}
    params_genius = {'q': song_name}
    response_genius = requests.get(base_url_genius + "/search", params=params_genius, headers=headers_genius).json()
    song_lyrics = response_genius['response']['hits'][0]['result']['url']
    return song_lyrics