#!/usr/bin/env python
import config
import time 
from controlmypi import ControlMyPi
import os 
import logging
import sys
from ampoule import *
from moisture import *
from AM2302 import *
from bmp183 import bmp183
from waterLevel import *
#13

def on_msg(conn, key, value):
    config.updateConfig(value, key)
    conn.update_status({'heure_jour_status':config.get('Heure_jour'), 'heure_nuit_status':config.get('Heure_nuit'), 'water_status':config.get('arrosage_auto'), 'seuil1_status':config.get('seuil1'), 'seuil2_status':config.get('seuil2'), 'seuil3_status':config.get('seuil3'), 'seuil4_status':config.get('seuil4'), 'arrosage_matin_status':config.get('arrosage_matin'), 'arrosage_soir_status':config.get('arrosage_soir') })
    pass
    
def append_chart_point(chart, point):
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
    [ ['O'] ],
    [ ['L','Lumiere artificielle'], ['S','lum_PIN','off'], ['L', 'Niveau d\'eau : '], ['I','water_level','#007BFF'] ],
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
    [ ['O'] ],
    [ ['L','Parametrage du jour et de la nuit:'] ],
    [ ['L','Heure Jour'], ['E','Heure_jour','Envoyer'], ['S','heure_jour_status',config.get('Heure_jour')] ], 
    [ ['L','Heure Nuit'], ['E','Heure_nuit','Envoyer'], ['S','heure_nuit_status',config.get('Heure_nuit')] ],
    [ ['C'] ],
    [ ['O'] ],
    [ ['L','Irrigation auto:'],['B','water_on','on'],['B','water_off','off'],['S','water_status', config.get('arrosage_auto')] ],
    [ ['C'] ],
    [ ['O'] ],
    [ ['L','Seuil humidite 1'], ['E','seuil1','Envoyer'], ['S','seuil1_status', config.get('seuil1')] ],
    [ ['L','Seuil humidite 2'], ['E','seuil2','Envoyer'], ['S','seuil2_status', config.get('seuil2')] ],       
    [ ['L','Seuil humidite 3'], ['E','seuil3','Envoyer'], ['S','seuil3_status', config.get('seuil3')] ],
    [ ['L','Seuil humidite 4'], ['E','seuil4','Envoyer'], ['S','seuil4_status', config.get('seuil4')] ],        
    [ ['L','Heure arrosage matin:'], ['E','arrosage_matin','Envoyer'] , ['S','arrosage_matin_status', config.get('arrosage_matin')]],            
    [ ['L','Heure arrosage soir:'], ['E','arrosage_soir','Envoyer'], ['S','arrosage_soir_status', config.get('arrosage_soir')] ],
    [ ['C'] ],
    ]
GPIO.setwarnings(False)
etat_ampoule = 'off'
light_off()
checkAmpoule()
bmp=bmp183()
conn = ControlMyPi('victorledeuff@xmpp.jp', 'mcs1aptesb1f', 'Potager2', 'capteurs2', p, on_msg)
print 'connexion...'
time.sleep(15)
if conn.start_control():
	try:
		 while True:

			#bmp=bmp183()
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
                        #Lumiere
			if isAmpouleOn() == 'on':
                        	result_lux = 100
                        else:
				result_lux = 0
			schart_lum = append_chart_point(schart_lum, int(result_lux))
	
			#temperature et humidite
			result_humidite, result_temperature = getHumTemp()
			schart_temp = append_chart_point(schart_temp, float(result_temperature))
			schart_hum = append_chart_point(schart_hum, float(result_humidite))
		    	
			#pression et temperature
			time.sleep(1)
			bmp.measure_pressure()
			#print "pressure", bmp.pressure/100
			#result_temperature = bmp.temperature
			#schart_temp = append_chart_point(schart_temp, float(result_temperature))
			result_pression = int(bmp.pressure/100)
                        schart_pression = append_chart_point(schart_pression, int(result_pression))
			
			etat_ampoule = isAmpouleOn()
			water_level = isWaterEmpty()

			conn.update_status({'water_level':water_level})	
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

