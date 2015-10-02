import RPi.GPIO as GPIO
#mode BCM

#Humidity sensor pin
tempHum_pin=21

# bmp183
spi_sck = 11 
spi_sdo= 9
spi_sdi=10
spi_cs=8

#pin on MCP3008
lux_pin=0 #Photoresistor
#moistures sensors are 1-4

# MCP3008
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25

#Ampoule
AMPOULE_PIN = 20 #for the relay supply module
heure_debut=9 #begin of light
heure_fin=21 #end (24h format)

#water motors pin
pin1=12 # motor one
pin2=5  # motor two
pulse=50
WATER_PIN = 16 #for the relay supply module



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
