#!/usr/bin/env python3

import time
import subprocess
#import readCard    - Commented out right now due to errors in readCard

print("Program Starting")

# opens the access list
accessFile = open("accessList.txt", "r")

# creates a list of strings with one ID number per string
accessList = accessFile.readlines()

accessFile.close()

# strips trailing new line characters from the list of strings.
#cardReader = MagSwipe()
accessList = [number.strip() for number in accessList]

while True:
  # Changed to raw_input, to not attempt to evaluate the input,
  # but simply keep it as a string.
  cardNum = raw_input('>>')

  # EE Milestone 2
  # cardNum = cardReader.wait_for_swipe()



  print "Input was", cardNum
  
  if cardNum == 'quit':
    break

  # CS Milestone 2
  # updateAccessList()
  # Query some remote list and update our own internal list

  if cardNum in accessList: 
    print("ID Successfully found in list. ACCESS GRANTED");
    # EE Milestone 1: Indicate success somehow!
    #subprocess.call("./relayON.sh")		 turns the relay on
    #time.sleep(6)				   
    #subprocess.call("./relayOFF.sh")  	 turns the relay off

  else: 
    print("ID Not found in list. ACCESS DENIED");




print("Thank you! Quitting.")
exit()
