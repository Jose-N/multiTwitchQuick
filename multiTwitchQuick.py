#! python3
# mulitTwitchQuick.py
# Launches a kadgar.net/live link using the Twitch usernames entered into the command line

import webbrowser,sys

# Grab usernames from command line
if len(sys.argv) > 1:
	if  "watch" == ''.join(sys.argv[1]):
		streams = []
		numStreams = input("How many channels do you want to watch?")
		for i in range(int(numStreams)):
			streams.append(input("What is the name of the channel?"))

# Open webbrowser
# Create kadgar link  