# Project 1 - Music Generator
## Clone the repo
`git clone https://github.com/NJIT-CS490-SP21/project1-mg657.git`
<br /> If you cd into the repository you'll see all the files
## APIs
Sign up for a Spotify Developer Account at [https://developer.spotify.com/](https://developer.spotify.com/)
## Install Requirements (if you don't already have them)
pip install python-dotenv
<br />pip install requests
<br />pip install Flask
## Setup
Create .env file in your main directory
<br />Add line: `export CLIENT_ID = 'YOUR_CLIENT_ID'`
<br />Add line: `export CLIENT_SECRET = 'YOUR_CLIENT_SECRET'`
## Run Application
Run command in terminal python main.py
<br />Preview web page in browser '/'
## Deploy to Heroku
Install Heroku CLI: `npm install -g heroku` 
<br />Create a free account on Heroku [https://signup.heroku.com/login](https://signup.heroku.com/login)
<br />Log in to Heroku: `heroku login -i`
<br />Create a Heroku app: `heroku create`
Push your code to Heroku's remote repository: `git push heroku main`
Open your app with your new URL: `heroku open` (Click the link to open if it doesn't open on its own)
<br />Go to [https://dashboard.heroku.com/apps](https://dashboard.heroku.com/apps) and click your App, then go to Settings, and click "Reveal Config Vars"
<br />Add your secret key from .env with the matching variable name (CLIENT_ID, CLIENT_SECRET) and value (your key). Once you refresh, you should see it running 
## What are at least 3 technical issues you encountered with your project? How did you fix them?
* In my index.html, my if statement would not work when I checked if the song preview URL existed. To fix this, I tried to look at whether my syntax was off and printing various variables. Through further searching, I eventually found out how to cast to a string [https://stackoverflow.com/questions/9856576/casting-ints-to-str-in-jinja2/19993378#19993378](https://stackoverflow.com/questions/9856576/casting-ints-to-str-in-jinja2/19993378#19993378), which I then used to compare them.
* Originally, when I displayed the artist, I always took the first item in the dictionary. However, I later realized that it did not always match the artist that corresponded to my artistID. To solve this, I created a for loop that listed out all the artists in the list so the user could see all the artists that collaborated on the song. 
* I was getting errors with getting the correct information from my json object, as at times the random song produced an out of bounds error. This is because I had the random number being picked from 0 to the length of the list. However, the way randint works, I had to subtract one, since lets say the artist had 10 songs and I wanted the last one. If I had random.randint(0,10), since the last song is at index 9, it would product an out of bounds error. To solve this, I had the number be picked from 0 to the length of the list minus 1 (random.randint(0,9)).
## What would you do to improve your project in the future?
* To improve my project in the future, I would provide the user the ability to choose one or multiple artists to generate songs from, provide song lyrics for the song, as well as display the corresponding music video through Youtube. I would also add a button, so the user would be able to add the song to a playlist on their Spotify account.