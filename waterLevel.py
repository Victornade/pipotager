#!/usr/bin/env python
 
import os 
import logging
import RPi.GPIO as GPIO
import sys
import config 

colemeter_pin=config.get('colemeter_pin')
GPIO.setup(colemeter_pin, GPIO.IN)

def isWaterEmpty():
	config.updateConfig(GPIO.input(colemeter_pin), "reservoir")
	if (GPIO.input(colemeter_pin)):
		return False
	else:
		return True
	
