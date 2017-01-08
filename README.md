# Unspotitracks
A small hacky python server to fetch unpopular tracks on Spotify regarding a query.

It can be useful if you want to discover new or less popular artists.

## How does it work ?
It first fetch public playlists regarding keywords entered into the search bar, then look for tracks into each playlist and filter them by low popularity. It finally shuffle them in order to generate more entropy in the process. The final result is a list of unpopular tracks on the scope of your search.

Popularity is defined by an integer from 0 to 100, with 100 the most popular song. It's based most of the time on the total number of plays the track has had and how recent those plays are. Generally speaking, songs that are being played a lot now will have a higher popularity than songs that were played a lot in the past. Note that the popularity value may lag actual popularity by a few days: the value is not updated in real time.

## Requirements
- Python 2.7 + `pip` >= v8.1.2
- Python dependencies
```
pip install -r requirements.txt
```

## Generate token
- Create a developer app on Spotify: https://developer.spotify.com/my-applications/#!/applications
- Don't forget to add a valid redirect URI in your app. For example `https://www.reddit.com`
- Then launch the interactive script to generate a new access token
```
$> python get_token.py
Please enter your spotify clientId
<your_clientId>
Please enter your spotify redirection uri
<your_redirection_uri>
Please enter the entire url where you have been redirected
<Should be the redirect uri + '?code=thecodeblabla'>
Please enter your spotify clientSecret
<your_clientSecret>
```

## Start the server
```
python server.py
```
Go to [http://localhost:8010](http://localhost:8010) and enjoy :)
