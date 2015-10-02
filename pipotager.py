#!/usr/bin/env python
from config import * 
import time 
from controlmypi import ControlMyPi
import os 
import logging
import sys
from ampoule import *
from moisture import *
from lux import *
from AM2302 import *
from bmp183 import bmp183
#13

def on_msg(conn, key, value):
    pass
    
def append_chart_point(chart, point):
    if chart[0] == 0 :
	chart = [point] * Qt;
    else : 
        chart = chart[1:]
    
    chart.append(point)
    return chart

def chart(chart):
    i=0
    schart = []
    while i<=(Qt-1) :
        schart.append([i+1,chart[i]])
        i=i+1
    return schart
#31
logging.basicConfig(level=logging.INFO)
Qt = 24*4
schart_temp = [0] * Qt
schart_mois1 = [0] * Qt
schart_mois2 = [0] * Qt
schart_mois3 = [0] * Qt
schart_mois4 = [0] * Qt
schart_mois5 = [0] * Qt
schart_hum = [0] * Qt
schart_lum = [0] * Qt
schart_pression = [0] * Qt
#41
p = [
    [ ['P','my_pic','https://dl.dropboxusercontent.com/u/1635283/applications/piplant/pushit/image_0.jpg'] ],
    [ ['L','Lumiere artificielle'], ['S','lum_PIN','off'] ],
    [ ['O'] ],
    [ ['L','Lumiere ambiante'], ['S','last_lumiere','0%'], ['L','Pression atmospherique'], ['S','last_pression','0hPa'] ],
    [ ['LC','lumiere','24h', 'pourcent',0,100],['L','  '], ['LC','pression','24h', 'hPa',900,1100],['L','  '], ],
    [ ['C'] ],
    [ ['O'] ],
    [ ['L','Humidite ambiante'], ['S','last_humidite','0%'], ['L','Temperature  ambiante'], ['S','last_temperature','0C'] ], 
    [ ['LC','humidite','24h','pourcent',0,100], ['L','  '], ['LC','temperature','24h', 'degrees',10,30],['L','  '] ],
    [ ['C'] ],
    [ ['L','Humidite du sol'] ],
    [ ['O'] ],
    [ ['L','Fraises: '],['S','last_moisture_1','0%'], ['L','Radis: '],['S','last_moisture_2','0%'] ],
    [ ['LC','moisture_1','24h', 'pourcent',0,100],['L','  '], ['LC','moisture_2','24h', 'pourcent',0,100],['L','  '] ],
    [ ['L','Salades: '],['S','last_moisture_3','0%'], ['L','Tomates cerises: '],['S','last_moisture_4','0%'] ],
    [ ['LC','moisture_3','24h', 'pourcent',0,100],['L','  '], ['LC','moisture_4','24h', 'pourcent',0,100],['L','  '] ],
    [ ['C'] ],
    ]
GPIO.setwarnings(False)
etat_ampoule = 'off'
light_off()
checkAmpoule()
bmp=bmp183()
conn = ControlMyPi('victorledeuff@xmpp.jp', 'mcs1aptesb1f', 'Potager', 'capteurs', p, on_msg)
print 'connexion...'

if conn.start_control():
	try:
		 while True:
			#humidite sol
			result_moisture1 = float(getMoisture(1))
			schart_mois1 = append_chart_point(schart_mois1, float(result_moisture1))                    

                        result_moisture2 = float(getMoisture(2))
                        schart_mois2 = append_chart_point(schart_mois2, float(result_moisture2))

                        result_moisture3 = float(getMoisture(3))
                        schart_mois3 = append_chart_point(schart_mois3, float(result_moisture3))

                        result_moisture4 = float(getMoisture(4))
                        schart_mois4 = append_chart_point(schart_mois4, float(result_moisture4))
			
		        result_moisture5 = float(getMoisture(5))
                        schart_mois5 = append_chart_point(schart_mois5, float(result_moisture5))

	
			#temperature et humidite
			result_humidite, result_temperature = getHumTemp()
			# schart_temp = append_chart_point(schart_temp, float(result_temperature))
			schart_hum = append_chart_point(schart_hum, float(result_humidite))
		    	
			#Lumiere
			result_lux = float(getLux())
			schart_lum = append_chart_point(schart_lum, int(result_lux))
			#pression et temperature
                        bmp.measure_pressure()
			result_temperature = bmp.temperature
			schart_temp = append_chart_point(schart_temp, float(result_temperature))
			result_pression = int(bmp.pressure/100)
                        schart_pression = append_chart_point(schart_pression, int(result_pression))
			
			etat_ampoule = isAmpouleOn()
			conn.update_status({'lum_PIN':etat_ampoule})
			conn.update_status({'last_pression':'{}hPa'.format(round(result_pression,2)),'last_temperature':'{}C'.format(round(result_temperature,2)), 'last_moisture_1':'{}%'.format(round(result_moisture1,2)), 'last_moisture_2':'{}%'.format(round(result_moisture2,2)), 'last_moisture_3':'{}%'.format(round(result_moisture3,2)), 'last_moisture_4':'{}%'.format(round(result_moisture4,2)),  'last_humidite':'{}%'.format(round(result_humidite,2)), 'last_lumiere':'{}%'.format(round(result_lux,2))})
			conn.update_status({'pression':chart(schart_pression), 'moisture_1':chart(schart_mois1), 'moisture_2':chart(schart_mois2), 'moisture_3':chart(schart_mois3), 'moisture_4':chart(schart_mois4), 'temperature':chart(schart_temp), 'humidite':chart(schart_hum), 'lumiere':chart(schart_lum)})
			conn.update_status({'my_pic':'https://dl.dropboxusercontent.com/u/1635283/applications/piplant/pushit/image_0.jpg'})	
		        minute = time.strftime('%M',time.localtime())
		        minute = int(minute)
			minute= 15 - minute%15
			time.sleep(minute*60)
	finally:
		conn.stop_control()
else:
	print("FAILED TO CONNECT")

