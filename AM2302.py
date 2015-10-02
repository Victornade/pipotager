#!/usr/bin/env python
import os 
import logging
import sys
import Adafruit_DHT
from config import *

def getTempHum_pin():
	return tempHum_pin
	
def getHumTemp():
	result_humidite, result_temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, tempHum_pin)
	return result_humidite, result_temperature

