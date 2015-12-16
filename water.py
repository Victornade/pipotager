

#!/usr/bin/env python
 

 
import os 
import logging
import RPi.GPIO as GPIO
import sys
from moisture import *
import time
import config
GPIO.setup(config.get('motor1_pin'),GPIO.OUT)
GPIO.setup(config.get('motor2_pin'),GPIO.OUT)
pwm1=GPIO.PWM(config.get('motor1_pin'),config.get('motor_pulse'))
pwm2=GPIO.PWM(config.get('motor2_pin'),config.get('motor_pulse'))
pwm1.start(5)
pwm2.start(5)
WATER_PIN=config.get('WATER_PIN')
GPIO.setup(WATER_PIN, GPIO.OUT)


def isWaterOn():
	if(GPIO.input(WATER_PIN) == 0):
		return 'on'
	else:
		return 'off'

def water_on():
	GPIO.output(WATER_PIN, GPIO.LOW)
	print 'Irrigation on'
def water_off():
	GPIO.output(WATER_PIN, GPIO.HIGH)
	print 'Irrigation off'

def checkWater():
	for i in range(2): #boucle 
		for pin in range(4): #Pour chaque pin:
			moisture = getMoisture(pin+1)
			limite=85
			if pin+1  == 1 :
				limite = config.get('seuil1')
			if pin+1 == 2 :
				limite = config.get('seuil2')
			if pin+1  == 3 :
				limite = config.get('seuil3')
			if pin+1 == 4 : 
				limite = config.get('seuil4')
			if moisture <= limite :
				arrose_plante(pin+1)
				arrose_plante(0)
			else:
				water_off()
		time.sleep(5)
	
def arrose(p):
	 i=5
	 if p == 4 :
	 	i=10
	 time.sleep(2)
	 water_on()
         time.sleep(i)
         water_off()
	 time.sleep(1)

def arrose_plante(p):
	if p==0 :
		#position nulle
		bouge_bras(3,11.5)
		time.sleep(1)
		repos()
	if p == 1:
		bouge_bras(5,12)
                arrose(p)
		bouge_bras(4.5,8)	
		arrose(p)
		bouge_bras(4.5,10.5)
                arrose(p)

	if p == 2:
		bouge_bras(7,11)
                arrose(p)
		bouge_bras(6,11)
                arrose(p)
		bouge_bras(7.7,10)
                arrose(p)
     		bouge_bras(7.7,9.5)
                arrose(p)
		bouge_bras(10,8.2)
                arrose(p)
	if p == 3:
		bouge_bras(5.5,9.5)
                arrose(p)
		bouge_bras(6,8)
                arrose(p)
		bouge_bras(7,8)
                arrose(p)
		bouge_bras(9,7)
                arrose(p)
		bouge_bras(8.7,7)
                arrose(p)
	if p == 4:
		bouge_bras(12,6.7)
                arrose(p)
		bouge_bras(12,6.2)
                arrose(p)
		bouge_bras(12,5.9)
                arrose(p)
	if p > 0:
		arrose_plante(0)			


def bouge_bras(m1, m2) :
	max=7
	for i in range(max) :
		pwm2.ChangeDutyCycle(12-(12-m2)/(max-i))
		pwm1.ChangeDutyCycle(3+(m1-3)/(max-i))
		time.sleep(0.1)

def repos() :
	pwm2.ChangeDutyCycle(0)
        pwm1.ChangeDutyCycle(0)
water_off()
arrose_plante(0)

