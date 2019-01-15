from ampoule import *
import time

while True:
	checkAmpoule()
	minute = time.strftime('%M',time.localtime())
        minute = int(minute)
	minute = 59- minute
	time.sleep(minute*60)


