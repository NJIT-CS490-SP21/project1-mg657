import requests
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, request
import random

app = Flask(__name__)
load_dotenv(find_dotenv())  # Load API keys from .env
AUTH_URL = "https://accounts.spotify.com/api/token"
auth_response = requests.post(
    AUTH_URL,
    {
        "grant_type": "client_credentials",
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
    },
)
auth_response_data = auth_response.json()
access_token = auth_response_data["access_token"]  # Save access token
headers_spotify = {
    "Authorization": "Bearer {token}".format(token=access_token)}
def get_artistID(endpoint):
    if endpoint == "artist":
        artist = request.form["Artist"]
        if len(artist) == 0: #if field was left blank, set default
            artist = "Logic"
        params_spotify_search = {
            "q": artist,
            "type": "track,artist",
        }  # Specify  parameter
        req_artist = requests.get(
            "https://api.spotify.com/v1/search",
            headers=headers_spotify,
            params=params_spotify_search).json() #get info using Spotify search API
        if len(req_artist["artists"]["items"]) == 0: #if artist is not valid, set default to Logic's Artist ID
            artist_id = "4xRYI6VqpkE3UwrDrAZL8L"
        else:
            artist_id = req_artist["artists"]["items"][0]["id"]
    else: # if the user would like a random song from my favorite artists
        artist_list = [             
            "3TVXtAsR1Inumwj472S9r4",  # Drake
            "06HL4z0CvFAxyc27GXpf02",  # Taylor Swift
            "66CXWjxzNUsdJxJ2JdwvnR",  # Ariana Grande
            "4xRYI6VqpkE3UwrDrAZL8L",  # Logic
            "4MCBfE4596Uoi2O4DtmEMz",  # Juice Wrld
            "1RyvyyTE3xzB2ZywiAwp0i",  # Future
            "07YZf4WDAMNwqr4jfgOZ8y",  # Jason Derulo
            "0C8ZW7ezQVs4URX5aX7Kqx",  # Selena Gomez
        ]
        rand_Artist = random.randint(
            0, len(artist_list)-1)  # picks random artist from list with index 0-7
        artist_id = artist_list[rand_Artist]
    return artist_id
    
def getSong(endpoint):
    if endpoint == "track": #if the user would like to get a random song from a specific year
        year = request.form["Year"] # Gets year from user input
        if len(year) != 4 or year.isdigit() == False: #checks if it is a four digit number, otherwise sets default
            year = "2020"
        params_spotify_year = { 
            'q': 'year:'+year, 
            'type': 'track'} #specify search parameter for tracks in given year
        req_song = requests.get('https://api.spotify.com/v1/search', 
        headers=headers_spotify,
        params=params_spotify_year).json() #get request using search API
        if(len(req_song['tracks']['items']) == 0): #if no tracks for given year, set default 
            year = '2020'
            params_spotify_year = { 'q': 'year:'+year, 
            'type': 'track'} #reset parameter with default
            req_song = requests.get('https://api.spotify.com/v1/search', 
            headers=headers_spotify,
            params=params_spotify_year).json() #get request with updated default parameter
        song_list = req_song['tracks']['items'] #generate list of songs
        counter = 0
        song_index=[]
        for i in song_list:
            release_date = i['album']['release_date'] #get release date for each song
            if year in release_date:
                song_index.append(counter) #only add the index if it is from the requested year
            counter=counter+1
        rand_song_ind = random.randint(0, len(song_index) - 1) #generate random number from list of valid songs
        rand_song = song_index[rand_song_ind] #get index of random song
        song = req_song['tracks']['items'][rand_song] #sets song information
        return generate(song)

def song_info(artist_id):
    params_spotify={ 'market': 'US'} # Specify market parameter
    req_artist_id = requests.get(
            'https://api.spotify.com/v1/artists/'+artist_id+'/top-tracks',
            headers=headers_spotify, 
            params=params_spotify).json() #Get request for top tracks based on given artist id
    rand_song = random.randint(0, len(req_artist_id["tracks"]) - 1)  # Picks random song from all the songs by given artist
    song = req_artist_id['tracks'][rand_song] #sets song information
    return generate(song)

def generate(song):
    song_name = song["name"]
    song_image = song["album"]["images"][1]["url"]
    song_prev_link = song["preview_url"]
    song_link = song["external_urls"]["spotify"]
    artist_name_list = song["artists"]
    artist_name = []
    for key in artist_name_list:  # For each item in list of artists
        artist_name.append(key["name"])  # Add the artist to the list
    return render_template(  # Send all info to html page
        "result.html",
        artist_name=artist_name,
        song_name=song_name,
        song_image=song_image,
        song_prev_link=song_prev_link,
        song_link=song_link,
        song_lyrics=lyricInfo(song_name),
        len=len(artist_name)
    )

def lyricInfo(song_name):
    base_url_genius = "http://api.genius.com"
    headers_genius = {'Authorization': 'Bearer ' + os.getenv("GENIUS_ACCESS_TOKEN")} #set header for Genius API
    params_genius = {'q': song_name}
    response_genius = requests.get(base_url_genius + "/search", 
    headers=headers_genius,
    params=params_genius).json() # Get request for lyrics
    if len(response_genius["response"]["hits"]) == 0: #if there are no lyrics for the song
        song_lyrics = "Sorry, there are no lyrics available for this song" # Set lyrics to specific message
    else:
        song_lyrics = response_genius["response"]["hits"][0]["result"]["url"] # Otherwise get the lyrics URL
    return song_lyrics