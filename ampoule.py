#!/usr/bin/env python
 

 
import time 
import os 
import logging
import RPi.GPIO as GPIO
import sys
from config import *

GPIO.setup(AMPOULE_PIN, GPIO.OUT)

def isAmpouleOn():
	if(GPIO.input(AMPOULE_PIN) == 0):
		return 'on'
	else:
		return 'off'

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
	heure = int(heure)
	
	if heure>=heure_debut and heure<heure_fin:
		light_on()
	else:
		light_off()


