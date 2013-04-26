#!/usr/bin/env python 3
#
# Jacob Melton
# Code is under public domain
#
# 

import time, subprocess, readCard, datetime
import RPi.GPIO as GPIO

print("Program Starting")
GPIO.setwarnings(False) #disable warnings because we know the pins are already enabled

GPIO.setmode(GPIO.BOARD) # initialize pin numbering in board mode
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # set pin 16 to be for output for acces sound
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # set pin 18 to be for output for denial sound

cardReader = readCard.MagSwipe # initialize a card reader
cardReader()	# set it up as a default reader

tempCardNum = cardReader().wait_for_swipe() #grab our first raw swipe

cardNum = ''.join(map(chr,tempCardNum[118:127])) # converts from list of ascii codes to string of chars removes school code from the info on the card so we just get the ID
print(cardNum)

while True:				    # asks for input reaptedly only way to quit is to send SIGINTER, program is mean to run continually
	accessFile = open("/usr/share/nginx/www/files/accessList.txt", "r")                 # opens the access list
	logFile = open("/home/pi/logFile.txt", "w")										# opens the log file in write mode
	accessList = accessFile.readlines()                         # creates a list of strings with one ID number per string
	accessFile.close()                          # close the file
	accessList = [number.strip() for number in accessList]      # strips trailing new line characters from the list of acces ID's

	if cardNum in accessList:			    # checks if input number is in accessList
		logOutput = datetime.datetime.now() + " User ID: " + cardNum + " | Access granted"
		logFile.write(logOutput)
		subprocess.call("./relayON.sh")	#turns the relay on
		GPIO.output(16, GPIO.HIGH) #output on pin 16
		time.sleep(5)	#for 5 seconds
		subprocess.call("./relayOFF.sh") #turns the relay off
		GPIO.output(16, GPIO.LOW) #turn it off cause we are done
	else:
		logOutput = datetime.datetime.now() + " User ID: " + cardNum + " | Access denied"
		logFile.write(logOutput)
		GPIO.output(18, GPIO.HIGH) #turn on denied sound
		time.sleep(5) 	#for 5 seconds
		GPIO.output(18, GPIO.LOW) # turn off denied sound

	tempCardNum = cardReader().wait_for_swipe()
	cardNum = ''.join(map(chr,tempCardNum[118:127])) # converts from list of ascii codes to string of chars removes school code from the info on the card so we just get the ID
	print(cardNum)
	logFile.close()

GPIO.cleanup()
