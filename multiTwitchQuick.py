#! python3
# mulitTwitchQuick.py
# Launches a kadgar.net/live link using the Twitch usernames entered into the command line

import webbrowser,sys,requests
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
#if len(sys.argv) > 1:
	#if  "live?" == ''.join(sys.argv[1]):
		# Grab list of channels I am following
		#following  = requests.get('http://www.twitch.tv/dark_fleet/profile/following')
		#following.raise_for_status()
		# Convert HTML to BeautifulSoup object
		#fText = BeautifulSoup(following.text, "html.parser")
		# Parse object for names of channels I am following
		#fList = fText.findAll("div", {"class" : "user item"})
		#users = fList.findAll("img")
		#print(str(len(fList)))
		#for i in range(len(fList)):
			#test = fText.select('img')[i]
			#print(test)