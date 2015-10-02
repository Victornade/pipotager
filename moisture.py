#!/usr/bin/env python
 

 
import time 
import os 
import logging
import RPi.GPIO as GPIO
import sys
from readMCP3008 import readadc

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


def getMoisture(pin):
	result_moisture = 0
	result_moisture = readadc(pin)
	result_moisture = (float(result_moisture)) / 1024 * 100
	result_moisture = int(result_moisture)
	result_moisture = 100 - result_moisture
	return result_moisture


