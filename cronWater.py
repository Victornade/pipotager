import water 
import config
import time

while True:
        heure = time.strftime('%H',time.localtime())
        heure = int(heure)
	if arrosage_auto == 'True':
	        if heure==config.get('arrosage_matin') or heure==config.get('arrosage_soir'):
	                water.checkWater()
        minute = time.strftime('%M',time.localtime())
        minute = int(minute)
        minute = 62- minute
        time.sleep(minute*60)
