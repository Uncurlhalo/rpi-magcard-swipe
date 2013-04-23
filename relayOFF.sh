#!/bin/bash
# sends the off signal to the USB relay
# You will need to add your self to the dialout group 
# and likely also nee to execute 'chmod a+rw /dev/ttyUSB0'
# to allow reading and writing to the device
echo -e "\xff\x01\x00" > /dev/ttyUSB0
echo "CLOSED"
