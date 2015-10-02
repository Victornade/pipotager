from ampoule import *
import time

while True:
	checkAmpoule()
	minute = time.strftime('%M',time.localtime())
        minute = int(minute)
	minute = 61- minute
	time.sleep(minute*60)


