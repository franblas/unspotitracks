import requests as rq
import base64
import webbrowser

raw_client_id = raw_input("Please enter your spotify clientId\n")
client_id = raw_client_id.strip()
raw_redirection_uri = raw_input("Please enter your spotify redirection uri\n")
redirection_uri = raw_redirection_uri.strip()
webbrowser.open("https://accounts.spotify.com/en/authorize?client_id=" + client_id + "&response_type=code&redirect_uri=" + redirection_uri,new=2)
raw_redirected_uri = raw_input("Please enter the entire url where you have been redirected (should be <your_redirection_uri>?code=<the_code>)\n")
code = raw_redirected_uri.split('?code=')[1].strip()
raw_client_secret = raw_input("Please enter your spotify clientSecret\n")
client_secret = raw_client_secret.strip()

data = {
    "grant_type": "authorization_code",
    "redirect_uri": redirection_uri,
    "code": code
}

headers = {
    'Authorization' : 'Basic ' + base64.standard_b64encode(client_id + ':' + client_secret)
}

rep = rq.post('https://accounts.spotify.com/api/token', data=data, headers=headers)
keys = rep.json()
if not keys:
    print "Oooopsss something goes wrong :("
    print rep
    print rep.json()

print 'Auth token successfuly generated!'
with open("auth_token", "w") as f:
    f.write(keys.get('access_token'))
