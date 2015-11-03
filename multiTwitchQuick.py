#! python3
# mulitTwitchQuick.py
# Launches a kadgar.net/live link using the Twitch usernames entered into the command line

import webbrowser,sys,requests, json
from bs4 import BeautifulSoup


if len(sys.argv) > 1:
	# Grab what channels to watch from cmd line, make kadgar, and launch browser
	if  "watch" == ''.join(sys.argv[1]):
		cmdline = ''.join(sys.argv[2:])
		streams = cmdline.split(",")
		# Create Kadgar link
		kadgar = "www.kadgar.net/live/"
		for i in range(len(streams)):
			kadgar = kadgar + streams[i] + "/"
		# Launch browser with link
		webbrowser.open(kadgar)
	# Print list of followed channels who are live, what game they are playing, and how many viwers
	elif  "live?" == ''.join(sys.argv[1]):
		getSourceChan = requests.get("https://api.twitch.tv/kraken/users/dark_fleet/follows/channels/?limit=100")
		textChan = json.loads(getSourceChan.text)
		channels = [] 
		for i in range(len(textChan["follows"])):
			channel = textChan["follows"][i]["channel"]["name"]
			getSourceStream = requests.get("https://api.twitch.tv/kraken/streams/" + channel)
			textStream = json.loads(getSourceStream.text)
			if textStream["stream"] != None: 
				game = textStream["stream"]["game"]
				viewers = str(textStream["stream"]["viewers"])
				try:
					print(channel + " is live playing " + game + " with " + viewers  + " viewers \n")
				except:
					print(channel + " is live, but not playing anything with " + viewers  + " viewers \n")
	# Help for commands
	elif "help" == ''.join(sys.argv[1]):
		print("The commands for these channels are: \n")
		print("<watch>: Grabs channel names from cmd line, makes a Kadgar link, and launches browser \n")
		print("<live?>: Print list of followed channels who are live, what game they are playing, and how many viwers \n")
	# Point user to help command, since what they typed wasn't an actual command
	else:
		print("Sorry but what you entered wasn't a commnd. Type <twitch help> to get a list of commands")