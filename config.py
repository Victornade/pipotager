import RPi.GPIO as GPIO
import ConfigParser

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
cfg= ConfigParser.ConfigParser()
path= '/home/pi/pipotager/config.cfg'

def updateConfig(value, key):        
	cfg.read(path)
        if key == 'water_on':
                cfg.set('config', 'arrosage_auto', 'On')
        elif key == 'water_off':
                cfg.set('config', 'arrosage_auto', 'Off')
        elif int(value) < 100:
                cfg.set('config', key, value)
        cfg.write(open(path,'w'))


def get(key):
        cfg.read(path)
	if key == 'arrosage_auto':
       		return cfg.get('config', key)
	else:
		 return cfg.getint('config', key)


