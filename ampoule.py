#!/usr/bin/env python
 

 
import time 
import os 
import logging
import RPi.GPIO as GPIO
import sys
import config 
AMPOULE_PIN= config.get('AMPOULE_PIN')
GPIO.setup(AMPOULE_PIN, GPIO.OUT)

def isAmpouleOn():
	if(GPIO.input(AMPOULE_PIN) == 0):
		return 'On'
	else:
		return 'Off'

def ampoule_PIN():
	return AMPOULE_PIN

def light_on():
	GPIO.output(AMPOULE_PIN, GPIO.LOW)
	print 'Ampoule allumee'
def light_off():
	GPIO.output(AMPOULE_PIN, GPIO.HIGH)
	print 'ampoule eteinte'

def checkAmpoule():
	heure = time.strftime('%H',time.localtime())
	heure = int(heure)+1
	if heure>=config.get('Heure_jour') and heure<config.get('Heure_nuit'):
		light_on()
	else:
		light_off()



print GPIO.input(AMPOULE_PIN)
