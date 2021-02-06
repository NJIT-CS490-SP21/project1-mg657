import requests
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
import random
app = Flask(__name__)
load_dotenv(find_dotenv()) # This is to load your API keys from .env
AUTH_URL = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('CLIENT_ID'),
    'client_secret': os.getenv('CLIENT_SECRET'),
}) 
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token'] #save access token
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
params={ 'market': 'US'}
artistID=['3TVXtAsR1Inumwj472S9r4', '6eUKZXaKkcviH0Ku9w2n3V', '66CXWjxzNUsdJxJ2JdwvnR', '4xRYI6VqpkE3UwrDrAZL8L','4MCBfE4596Uoi2O4DtmEMz','1RyvyyTE3xzB2ZywiAwp0i','07YZf4WDAMNwqr4jfgOZ8y','0C8ZW7ezQVs4URX5aX7Kqx']
#Artists: Drake, Ed Sheeran, Ariana Grande, Logic, Juice Wrld, Future, Jason Derulo, Selena Gomez

@app.route('/')
def songInfo():
    rand_Artist = random.randint(0,7) #picks random artist from list with index 0-7
    BASE_URL = 'https://api.spotify.com/v1/artists/' #Base URL for get request
    req = requests.get(BASE_URL+artistID[rand_Artist]+'/top-tracks', headers=headers, params=params).json() #GET request
    rand_song = random.randint(0,len(req['tracks'])-1) #picks random song from all the songs by certain artist
    global artistList
    global artistName
    artistList=req['tracks'][rand_song]['artists']
    songName=req['tracks'][rand_song]['name']
    songImage=req['tracks'][rand_song]['album']['images'][1]['url']
    songURL=req['tracks'][rand_song]['preview_url']
    for i in range(len(artistList)): #range(len) prints indexes
        if (artistList[i]['id']==artistID[rand_Artist]): 
            artistName = req['tracks'][rand_song]['artists'][i]['name']
        break
    return render_template( #send all info to html page
        'index.html',
        artistName=artistName,
        songName=songName,
        songImage=songImage,
        songURL=songURL
        )
app.run(
    port=int(os.getenv('PORT',8080)), 
    host=os.getenv('IP','0.0.0.0'),
    debug=True
    )