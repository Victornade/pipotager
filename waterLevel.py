#!/usr/bin/env python
 
import os 
import logging
import RPi.GPIO as GPIO
import sys
import config 

colemeter_pin=config.get('colemeter_pin')
GPIO.setup(colemeter_pin, GPIO.IN)

def isWaterEmpty():
	if (GPIO.input(colemeter_pin)):
		return '#007BFF'
	else:
		return '#ff0000'
	
