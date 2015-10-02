

#!/usr/bin/env python
 

 
import os 
import logging
import RPi.GPIO as GPIO
import sys
from moisture import *
import time
from config import *
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
pwm1=GPIO.PWM(pin1,pulse)
pwm2=GPIO.PWM(pin2,pulse)
pwm1.start(5)
pwm2.start(5)
GPIO.setup(WATER_PIN, GPIO.OUT)

def isWaterOn():
	if(GPIO.input(WATER_PIN) == 0):
		return 'on'
	else:
		return 'off'

def water_PIN():
	return WATER_PIN
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
			if moisture <= 85 :
				arrose_plante(pin+1)
				arrose_plante(0)
			else:
				water_off()
		time.sleep(5)
	
def arrose():
	i=5
	time.sleep(2)
	water_on()
        time.sleep(i)
        water_off()
	time.sleep(1)

def arrose_plante(p):
	if p==0 :
		#position nulle
		pwm1.ChangeDutyCycle(8)
                pwm2.ChangeDutyCycle(10.5)
		time.sleep(0.5)
		pwm1.ChangeDutyCycle(0)
                pwm2.ChangeDutyCycle(0)
	if p == 1:
		pwm1.ChangeDutyCycle(4.5)
		pwm2.ChangeDutyCycle(8)	
		arrose()
		pwm1.ChangeDutyCycle(4.5)
                pwm2.ChangeDutyCycle(10.5)
                arrose()

	if p == 2:
                pwm1.ChangeDutyCycle(7.5)
                pwm2.ChangeDutyCycle(11)
                arrose()
                pwm1.ChangeDutyCycle(6.2)
                pwm2.ChangeDutyCycle(11)
                arrose()
                pwm1.ChangeDutyCycle(7.7)
                pwm2.ChangeDutyCycle(10)
                arrose()
                pwm1.ChangeDutyCycle(12)
                pwm2.ChangeDutyCycle(7.7)
                arrose()
                pwm1.ChangeDutyCycle(10)
                pwm2.ChangeDutyCycle(8.2)
                arrose()
	if p == 3:
                pwm1.ChangeDutyCycle(5.5)
                pwm2.ChangeDutyCycle(9.5)
                arrose()
                pwm1.ChangeDutyCycle(6)
                pwm2.ChangeDutyCycle(8)
                arrose()
                pwm1.ChangeDutyCycle(7)
                pwm2.ChangeDutyCycle(8)
                arrose()
                pwm1.ChangeDutyCycle(9)
                pwm2.ChangeDutyCycle(7)
                arrose()
                pwm1.ChangeDutyCycle(8.7)
                pwm2.ChangeDutyCycle(8)
                arrose()
	if p == 4:
                pwm2.ChangeDutyCycle(6.7)
		time.sleep(0.3)
                pwm1.ChangeDutyCycle(12)
                arrose()
                pwm1.ChangeDutyCycle(12)
                pwm2.ChangeDutyCycle(6.2)
                arrose()
                pwm1.ChangeDutyCycle(12)
                pwm2.ChangeDutyCycle(5.4)
                arrose()
	if p > 0:
		arrose_plante(0)			

arrose_plante(0)
water_off()
