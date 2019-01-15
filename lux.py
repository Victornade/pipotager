import time

import os

import logging

import RPi.GPIO as GPIO

import sys

from readMCP3008 import readadc

import config

# change these as desired - they're the pins connected from the

# SPI port on the ADC to the Cobbler



def getLux():

        result = 0

        result = readadc(0)
	
        result = (float(result)) / 1024 * 100

        result = int(result)

        #result_moisture = 100 - result_moisture

        return result


if __name__ == '__main__':
	print getLux()
	sys.exit(getLux())
