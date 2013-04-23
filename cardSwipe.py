#!/usr/bin/env python 3
#
# Jacob Melton
# Code is under public domain
#
# 

import time, subprocess, readCard

print("Program Starting")

cardReader = readCard.MagSwipe
cardReader()
tempCardNum = cardReader().wait_for_swipe()

cardNum = ''.join(map(chr,tempCardNum[118:127])) # converts from list of ascii codes to string of chars removes school code from the info on the card so we just get the ID
print(cardNum)

while True:				    # asks for input reaptedly only way to quit is to send SIGINTER, program is mean to run continually
	accessFile = open("/usr/share/nginx/www/files/accessList.txt", "r")                 # opens the access list
	accessList = accessFile.readlines()                         # creates a list of strings with one ID number per string
	accessFile.close()                          # close the file
	accessList = [number.strip() for number in accessList]      # strips trailing new line characters from the list of acces ID's

	if cardNum in accessList:			    # checks if input number is in accessList
		subprocess.call("./relayON.sh")	#turns the relay on
		time.sleep(6)
		subprocess.call("./relayOFF.sh") #turns the relay off
	else:
		print("ID not in Access List - Access Denied!")

	tempCardNum = cardReader().wait_for_swipe()
	cardNum = ''.join(map(chr,tempCardNum[118:127])) # converts from list of ascii codes to string of chars removes school code from the info on the card so we just get the ID
	print(cardNum)
