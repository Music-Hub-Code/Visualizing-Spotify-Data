import sys
import json
import spotipy.util as util
import requests
import pprint
import csv

def my_top_tracks(username, limit=1):
	token = util.prompt_for_user_token(username, "user-top-read")
	if token:
		response = requests.get("https://api.spotify.com/v1/me/top/tracks?limit="+str(limit), headers={"Authorization": "Bearer "+token})
		data = json.loads(response.text)
		with open('Top Tracks.csv', 'w') as csvfile:
			fieldnames = ['TrackName', 'ArtistName', 'MyRanking', 'GlobalPopularity', 'Loudness', 'Tempo']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for item in range (0, len(data['items'])):
				track = data['items'][item]['name']
				print "Crunching",'"'+track+'"'
				artist = data['items'][item]['artists'][0]['name'].encode('utf-8')
				popularity = data['items'][item]['popularity']
				# Look up song features
				songID = data['items'][item]['id']
				analysisResponse = requests.get("https://api.spotify.com/v1/audio-analysis/"+songID, headers={"Authorization": "Bearer "+token})
				analysisData = json.loads(analysisResponse.text)
				songDecibels = analysisData['track']['loudness']
				songTempo = analysisData['track']['tempo']
				writer.writerow({'TrackName': track, 'ArtistName': artist, 'MyRanking': str(item+1), 'GlobalPopularity': popularity, 'Loudness': songDecibels, 'Tempo': songTempo})
	else:
		print "Can't get token for", username

def tracks_by_time(username,limit=1):
	token = util.prompt_for_user_token(username, "user-read-recently-played")
	if token:
		response = requests.get("https://api.spotify.com/v1/me/player/recently-played?&after=1499472000&limit="+str(limit), headers={"Authorization": "Bearer "+token})
		data = json.loads(response.text)
		with open('Recents.csv', 'w') as csvfile:
			fieldnames = ['TrackName', 'ArtistName', 'Date', 'Time','Loudness','Tempo']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for item in range (0, len(data['items'])):
				track = data["items"][item]['track']['name']
				print "Crunching",'"'+track+'"'
				artist = data["items"][item]['track']['artists'][0]['name'].encode('utf-8')
				dateString = data["items"][item]['played_at']
				dateArray = dateString.split('T')
				date = dateArray[0]
				timeString = dateArray[1]
				timeArray = timeString.split(':')
				# Put in Toronto Timezone
				hours = str(int(timeArray[0])-3)
				time = hours+':'+timeArray[1]
				# Look up song features
				songID = data['items'][item]['track']['id']
				analysisResponse = requests.get("https://api.spotify.com/v1/audio-analysis/"+songID, headers={"Authorization": "Bearer "+token})
				analysisData = json.loads(analysisResponse.text)
				songDecibels = analysisData['track']['loudness']
				songTempo = analysisData['track']['tempo']
				writer.writerow({'TrackName': track, 'ArtistName': artist, 'Date':date, 'Time':time, 'Loudness':songDecibels,'Tempo':songTempo})
	else:
		print "Can't get token for", username

def read_dailyMix(username):
	playlistID = "0wrIbIqlJajjvxyojOQFAb"
	token = util.prompt_for_user_token(username,)
	if token:
		response = requests.get("https://api.spotify.com/v1/users/bengahtan/playlists/"+playlistID+"/tracks", headers={"Authorization": "Bearer "+token})
		data = json.loads(response.text)
		with open('Daily Mix.csv', 'w') as csvfile:
			fieldnames = ['TrackName', 'ArtistName', 'PlaylistRanking', 'GlobalPopularity', 'Loudness','Tempo']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for item in range (0,len(data['items'])):
				track = data["items"][item]['track']['name']
				print "Crunching",'"'+track+'"'
				artist = data["items"][item]['track']['artists'][0]['name'].encode('utf-8')
				popularity = data['items'][item]['track']['popularity']
				songID = data['items'][item]['track']['id']
				analysisResponse = requests.get("https://api.spotify.com/v1/audio-analysis/"+songID, headers={"Authorization": "Bearer "+token})
				analysisData = json.loads(analysisResponse.text)
				songDecibels = analysisData['track']['loudness']
				songTempo = analysisData['track']['tempo']
				writer.writerow({'TrackName': track, 'ArtistName': artist, 'PlaylistRanking':str(item+1), 'GlobalPopularity':popularity, 'Loudness':songDecibels,'Tempo':songTempo})
	else:
		print "Can't get token for", username

if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print "Whoops, need your username!"
        print "usage: python spotify.py [username]"
        sys.exit()
    # OPTIONS: run my_top_tracks(username,50), tracks_by_time(username,50), or read_dailyMix(username)
    read_dailyMix("bengahtan")
