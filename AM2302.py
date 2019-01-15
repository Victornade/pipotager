#!/usr/bin/env python
import os 
import logging
import sys
import Adafruit_DHT
import config


def getHumTemp():
	result_humidite, result_temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, config.get('AM2302_pin'))
	print result_humidite
	print result_temperature
	return result_humidite, result_temperature

if __name__ == '__main__':
	a,b=getHumTemp()
