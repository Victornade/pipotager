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

def getValue():
	result = 0
	result = readadc(7)
	result = (float(result)) #/ 1024 * 100
	result = int(result)
	#result = 500 - result
	return result

if __name__ == '__main__':
	while True:
		print getValue()
		time.sleep(1)
