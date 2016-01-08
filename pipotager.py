#!/usr/bin/env python
import config
import csv
import time 
import os 
import logging
import sys
from ampoule import *
from moisture import *
from AM2302 import *
from bmp183 import bmp183
from waterLevel import *
#13

GPIO.setwarnings(False)
etat_ampoule = 'off'
light_off()
checkAmpoule()
bmp=bmp183()

while True:
			#humidite sol
			result_moisture1 = round(float(getMoisture(1)),2)
                        result_moisture2 = round(float(getMoisture(2)),2)
                        result_moisture3 = round(float(getMoisture(3)),2)
                        result_moisture4 = round(float(getMoisture(4)),2)
		        result_moisture5 = round(float(getMoisture(5)),2)
                        #Lumiere
			if isAmpouleOn() == 'On':
                        	result_lux = 100
                        else:
				result_lux = 0
	
			#temperature et humidite

			result_humidite, result_temperature = getHumTemp()
			result_temperature = round(result_temperature,1)
			result_humidite = round(result_humidite,2)
		    	
			#pression et temperature
			time.sleep(1)
			bmp.measure_pressure()
			result_pression = round(int(bmp.pressure/100),1)
			
			etat_ampoule = isAmpouleOn()
			if (isWaterEmpty()) :
				config.updateConfig("Off", "arrosage_auto")
			
			datafile=open('datas.csv', 'a')
			c = csv.writer(datafile)
			moisturefile=open('moistures.csv', 'a')
			csvmoisture = csv.writer(moisturefile)
			c.writerow([time.strftime('%Y/%m/%d %H:%M',time.localtime()), result_lux, result_temperature, result_pression])	
			csvmoisture.writerow([time.strftime('%Y/%m/%d %H:%M',time.localtime()), result_humidite, result_moisture1, result_moisture2, result_moisture3, result_moisture4])
			moisturefile.close()
			datafile.close()
		        minute = time.strftime('%M',time.localtime())
		        minute = int(minute)
			minute= 15 - minute%15
			print "sleep"
			time.sleep(minute*60)	

