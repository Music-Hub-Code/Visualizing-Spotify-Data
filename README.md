# Visualizing-Spotify-Data
Github repo to complement https://begahtan.github.io/2017/07/visualizing-spotify.html
<br>

# How does it work?

Using Spotify API, that's all.

Requirement

This tool is built by Python 2 and uses requests module for querying the API and the spotipy library for OAuth.

Please make sure that you have already installed requests and spotipy.

If not, you can use pip to install:

pip install requests

pip install spotipy

# How to use?

python spotify.py username

Because it was made using functional programming, you can modify the tool to suit your data collection needs! See (the Spotify API Endpoints) for the data you can collect.

The functions I have created are:
- my_top_tracks(username,amountToOutput) => see your top tracks outputted in Excel and their attributes
- tracks_by_time(username,amountToOutput) => see the timestamps for your past tracks outputted in Excel and their attributes
- read_dailyMix(username) => see the songs in your daily mix and their attributes

Feel free to use these, comment them out, or create your own!
