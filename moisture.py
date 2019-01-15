#!/usr/bin/env python
 

 
import time 
import os 
import logging
import RPi.GPIO as GPIO
import sys
from readMCP3008 import readadc
import config
# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler

def getMoisture(pin):
	result_moisture = 0
	result_moisture = readadc(pin)
	#print str(pin) + ' : ' + str(result_moisture)
	result_moisture = (float(result_moisture)) / 1024 * 100
	result_moisture = int(result_moisture)
	result_moisture = 100 - result_moisture
        print str(pin) + ' : ' + str(result_moisture)

	return result_moisture


if __name__ == '__main__' :
	while True :
		getMoisture(0)
                getMoisture(1)
                getMoisture(2)
		time.sleep(0.1)
                getMoisture(3)
                getMoisture(4)
                getMoisture(5)
                getMoisture(6)
                getMoisture(7)
		print ' '
		time.sleep(1)

