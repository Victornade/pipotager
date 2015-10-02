
#!/usr/bin/env python
 

from config import * 
import os 
import sys
from readMCP3008 import readadc



def lux_PIN():
	return lux_pin

def getLux():
	result_lux = 0.0
	result_lux = readadc(lux_pin)
	result_lux  = (1+float(result_lux)) / 1024 *100 
	if result_lux > 5:
		result_lux = 100
	else :
		result_lux = 0
	return result_lux


