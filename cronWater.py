import water 
import config
import time
import waterLevel

while True:
        heure = time.strftime('%H',time.localtime())
        heure = int(heure)
	if config.get("arrosage_auto") == 'On' and  waterLevel.isWaterEmpty() == False :
		print "pas vide, arrosage on"
		if heure==config.get('arrosage_matin') or heure==config.get('arrosage_soir'):
			water.checkWater()
        minute = time.strftime('%M',time.localtime())
        minute = int(minute)
        minute = 62- minute
        time.sleep(minute*60)
