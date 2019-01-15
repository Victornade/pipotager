#!/usr/bin/env python
import config
import csv
import time 
import os 
import logging
import sys
print("import library")
from ampoule import *
from lux import *
print("import ampoule")
from moisture import *
print("import moisture")
from AM2302 import *
print("import am2302")
from bmp183 import bmp183
print("import bmp183")
from waterLevel import *
print("import airQuality")
import airQuality as air 
import bdd as bdd
#13

print("import ok")
GPIO.setwarnings(False)
etat_ampoule = 'off'
light_off()
checkAmpoule()
bmp=bmp183()
print("while")
while True:
			#humidite sol
			result_moisture1 = round(float(getMoisture(1)),2)
                        result_moisture2 = round(float(getMoisture(2)),2)
                        result_moisture3 = round(float(getMoisture(3)),2)
                        result_moisture4 = round(float(getMoisture(4)),2)
		        result_moisture5 = round(float(getMoisture(5)),2)
                        result_moisture6 = round(float(getMoisture(6)),2)
			print("moisture")
			print(result_moisture1)
                        print(result_moisture2)
                        print(result_moisture3)
                        print(result_moisture4)
                        print(result_moisture5)
                        print(result_moisture6)
			#Lumiere
			#if isAmpouleOn() == 'On':
                        #	result_lux = 100
                        #else:
			#	result_lux = 0
			result_lux=round(float(getLux()),2)
			#temperature et humidite
			
			airQ=air.getValue()

			result_humidite, result_temperature = getHumTemp()
			result_temperature = round(result_temperature,1)
			result_humidite = round(result_humidite,2)
		    	print("temperature / humidite")
			print(result_temperature)
			print(result_humidite)
			#pression et temperature
			time.sleep(1)
			bmp.measure_pressure()
			print("temp / pression")
			print(bmp.measure_temperature())
			result_pression = round(int(bmp.pressure/100),1)
			print(result_pression)			
			etat_ampoule = isAmpouleOn()
			#if (isWaterEmpty()) :
			#	config.updateConfig("Off", "arrosage_auto")
			
			datafile=open('/home/pi/datas.csv', 'a')
			c = csv.writer(datafile)
			moisturefile=open('/home/pi/moistures.csv', 'a')
			csvmoisture = csv.writer(moisturefile)
			c.writerow([time.strftime('%Y/%m/%d %H:%M',time.localtime()), result_lux, result_temperature, result_pression, airQ])	
			csvmoisture.writerow([time.strftime('%Y/%m/%d %H:%M',time.localtime()), result_humidite, result_moisture1, result_moisture2, result_moisture3, result_moisture4])
			moisturefile.close()
			datafile.close()

			bdd.insertDatas(result_temperature, result_humidite, result_pression, result_lux, airQ, result_moisture1,result_moisture2, result_moisture3,result_moisture4, result_moisture5, result_moisture6)
		        #insertDatas(temp, humidite, pression, lumiere, air, hum1,hum2,hum3,hum4, hum5, hum6)
			minute = time.strftime('%M',time.localtime())
		        minute = int(minute)
			minute= 15 - minute%15
			print "sleep"
			time.sleep(minute*60)	

