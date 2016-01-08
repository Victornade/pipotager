import RPi.GPIO as GPIO
import ConfigParser

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
cfg= ConfigParser.ConfigParser()
path= '/home/pi/pipotager/config.cfg'

def updateConfig(value, key):        
	cfg.read(path)
        if key == 'arrosage_auto':
                cfg.set('config', 'arrosage_auto', value)
        elif int(value) < 100:
                cfg.set('config', key, value)
        cfg.write(open(path,'w'))


def get(key):
        cfg.read(path)
	if key == 'arrosage_auto':
       		return cfg.get('config', key)
	else:
		 return cfg.getint('config', key)


