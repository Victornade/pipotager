from water import *
import time

while True:
        heure = time.strftime('%H',time.localtime())
        heure = int(heure)
        if heure>=11 and heure<19:
                checkWater()
        minute = time.strftime('%M',time.localtime())
        minute = int(minute)
        minute = 62- minute
        time.sleep(minute*60)
