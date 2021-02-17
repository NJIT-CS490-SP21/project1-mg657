# Project 1 - Music Generator
Preview Application: [https://glacial-inlet-25895.herokuapp.com/](https://glacial-inlet-25895.herokuapp.com/)
## Clone the repo
CLI Command: `git clone https://github.com/NJIT-CS490-SP21/project1-mg657`
<br /> If you cd into the repository you'll see all the files
## APIs
Sign up for a Spotify Developer Account at [https://developer.spotify.com/](https://developer.spotify.com/)
Register your application for Genius API [https://docs.genius.com/#/getting-started-h1](https://docs.genius.com/#/getting-started-h1)
## Install Requirements (if not already installed)
`pip install python-dotenv`
<br />`pip install requests`
<br />`pip install Flask`
## Setup
Create .env file in your main directory
<br />Add line: `export CLIENT_ID = 'YOUR_CLIENT_ID'`
<br />Add line: `export CLIENT_SECRET = 'YOUR_CLIENT_SECRET'`
<br />Add line: `export GENIUS_ACCESS_TOKEN = 'YOUR_GENIUS_ACCESS_TOKEN'`
## Run Application
Run the application in terminal using `python main.py`
<br />Preview the web page in browser '/'
## Deploy to Heroku
Install Heroku CLI: `npm install -g heroku` 
<br />Create a free account on Heroku [https://signup.heroku.com/login](https://signup.heroku.com/login)
<br />Log in to Heroku: `heroku login -i`
<br />Create a Heroku app: `heroku create`
<br />Push your code to Heroku's remote repository: `git push heroku main`
<br />Open your app with your new URL: `heroku open`
<br />Go to [https://dashboard.heroku.com/apps](https://dashboard.heroku.com/apps) and click your App, then go to Settings, and click "Reveal Config Vars"
<br />Add your secret key from .env with the matching variable name (CLIENT_ID, CLIENT_SECRET, GENIUS_ACCESS_TOKEN) and value (your key). Once you refresh, it should run
## What are at least 3 technical issues you encountered with your project? How did you fix them?
* In my index.html, my if statement would not work when I checked if the song preview URL existed. To fix this, I tried to look at whether my syntax was off and printing various variables. Through further searching, I eventually found out how to cast to a string [https://stackoverflow.com/questions/9856576/casting-ints-to-str-in-jinja2/19993378#19993378](https://stackoverflow.com/questions/9856576/casting-ints-to-str-in-jinja2/19993378#19993378), which I then used to compare them.
* I was getting errors with getting the correct information from my json object, as at times the random song produced an out of bounds error. This is because I had the random number being picked from 0 to the length of the list. However, the way randint works, I had to subtract one, since lets say the artist had 10 songs and I wanted the last one. If I had random.randint(0,10), since the last song is at index 9, it would produce an out of bounds error. To solve this, I had the number be picked from 0 to the length of the list minus 1 (random.randint(0,9)).
* I was having trouble implementing the search feature, meaning when the user hit submit, I wanted to manipulate the input they entered. After many Google searches, I came across this helpful link describing how exactly to take the input entered and display it on another page, which helped serve as the basis on how to expand upon the implementation. [https://pythonbasics.org/flask-template-data/](https://pythonbasics.org/flask-template-data/)
* Originally, when I tried to manipulate the user data, if the user inputted invalid data (for example, in the Year text field they inputted 'hello') the API calls would result in an error page being generated. To solve this, I went through my code line by line, using many print statements to understand where the code was getting stuck. I then figured out what variables had to be set and when to perform another GET request from the API. For example, if the user leaves the field blank and clicks the artist button, they will see a randomly generated song by Logic. Similarly, if the user leaves the field blank and clicks the year button, they will see a randomly generated song from the year 2020.
## What are known problems (still existing), if any, with your project? 
* The lyrics don't always generate for certain songs, so in that case, the application generates a message indicating the lyrics could not be found.
* The song preview link does not always generate, so in the case that it does not, I display a link to the song on Spotify.
## What would you do to improve your project in the future?
* To improve my project in the future, I would provide the user the ability to add the generated song to their playlist, display the corresponding music video using the Youtube API, and provide them with the ability to see similar song recommendations using the Spotify API. I would also add a Home button for a better user experience. 