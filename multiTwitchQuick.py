#! python3
# mulitTwitchQuick.py
# Launches a kadgar.net/live link using the Twitch usernames entered into the command line

import webbrowser,sys,requests, json
from bs4 import BeautifulSoup

# Grab usernames from command line
if len(sys.argv) > 1:
	if  "watch" == ''.join(sys.argv[1]):
		cmdline = ''.join(sys.argv[2:])
		streams = cmdline.split(",")
		# Create Kadgar link
		kadgar = "www.kadgar.net/live/"
		for i in range(len(streams)):
			kadgar = kadgar + streams[i] + "/"
		webbrowser.open(kadgar)

# TODO: Add ability to see who is live and for how long they have been live
#### This might require some working with Java Script, need to reasearch ####
if len(sys.argv) > 1:
	if  "live?" == ''.join(sys.argv[1]):
		getSourceChan = requests.get("https://api.twitch.tv/kraken/users/dark_fleet/follows/channels/?limit=100")
		textChan = json.loads(getSourceChan.text)
		for i in range(len(textChan["follows"])):
			channel  = textChan["follows"][i]["channel"]["name"]
			getSourceStream = requests.get("https://api.twitch.tv/kraken/streams/" + channel)
			textStream = json.loads(getSourceStream.text)
			if textStream["stream"] != None: 
				print(textStream["stream"]["channel"]["name"] + " is live playing " + textStream["stream"]["game"] + " with " +  str(textStream["stream"]["viewers"]) + " viewers \n")
			
