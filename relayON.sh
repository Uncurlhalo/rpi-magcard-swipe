#!/bin/bash
# sends on signal to the USB relay
# You will need to add your self to the dialout group 
# and likely also nee to execute 'chmod a+rw /dev/ttyUSB0'
# to allow reading and writing to the device
echo -e "\xFF\x01\x01" > /dev/ttyUSB0
echo "OPENED"
