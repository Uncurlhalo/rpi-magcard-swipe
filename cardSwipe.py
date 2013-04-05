import time
import subprocess

print("Program Starting")

accessFile = open("accessList.txt", "r")    	            # opens the access list
accessList = accessFile.readlines()			    # creates a list of strings with one ID number per string
accessFile.close()					    # close the file

accessList = [number.strip() for number in accessList]	    # strips trailing new line characters from the list of strings.

while True:					  	    # python do while, gets card input, if it isnt right length then repeats
	cardNum = input('>>')				    # breaks on proper length string
	if len(cardNum) == 9:
		break

while cardNum != "quit":				    # asks for input reaptedly
	if cardNum in accessList:			    # checks if input number is in accessList
		subprocess.call("./relayON.sh")		    # turns the relay on
		time.sleep(6)				    # waits a few seconds to let them open the door
		subprocess.call("./relayOFF.sh")  	    # turns the relay off
	else:
		print("ID not in Access List - Access Denied!")

	while True:                                         # do repeatedly till we get good input
		cardNum = input('>>')
		if len(cardNum) == 9 or cardNum == "quit":  # check we are getting the right length ID or are quiting
			break

print("You have quit")
exit()
