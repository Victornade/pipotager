
#!/usr/bin/env python

import os
import logging
import sys
#from water import *
from ampoule import *
from moisture import *
from lux import *
from AM2302 import *
from bmp183 import bmp183

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
bmp=bmp183()


#humidite sol

result_moisture1 = float(getMoisture(1))

print 'humidite 1:', result_moisture1

result_moisture2 = float(getMoisture(2))

print 'humidite 2:', result_moisture2

result_moisture3 = float(getMoisture(3))

print 'humidite 3:', result_moisture3

result_moisture4 = float(getMoisture(4))

print 'humidite 4:', result_moisture4


#temperature et humidite
result_humidite, result_temperature = getHumTemp()
# schart_temp = append_chart_point(schart_temp, float(result_temperature))
print 'humidite air:', result_humidite
#Lumiere
result_lux = float(getLux())
print 'lumiere:', result_lux
#pression et temperature
bmp.measure_pressure()
result_temperature = bmp.temperature
print 'temperature ', result_temperature
result_pression = float(bmp.pressure/100)
print 'pression ', result_pression


