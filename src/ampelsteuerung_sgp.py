# Ampelsteuerung zur Anzeige der Luftqualität im Raum 
# gemessen werden eCO2 un TVOC

# Alle 3 Sekunden wird die Luftquatlität gemessen

import time
import board
import busio
import mraa
import adafruit_sgp30

IN = 0
OUT = 1
LOW = 0
HIGH = 1

from adafruit_blinka.microcontroller.am654 import pin   

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

print("SGP30 serial #", [hex(i) for i in sgp30.serial])

sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8AAE)

elapsed_sec = 0

#LEDs über Klasse Pin als OUTPUT deglarieren
LED4 = pin.D4
LED4.init(OUT)              

LED5 = pin.D5
LED5.init(OUT)

LED8 = pin.D8
LED8.init(OUT)


try:
                            
    while True: 
	
        if (sgp30.eCO2 > 2000 or sgp30.TVOC > 10):    # Angabe der Sensorwerte in ppm
            LED4.value(LOW)
            LED5.value(HIGH)                          # LED D5 soll leuchten 
            LED8.value(LOW)                  
            print("Es muss jetzt gelüftet werden, die Luftqualtiät ist schlecht.")
            time.sleep(3)                             # Zeitverzögerung von 3 Sekunden
		
        elif (sgp30.eCO2 >= 1000 or sgp30.TVOC >= 5): # Angabe der Sensorwerte in ppm
            LED4.value(HIGH)                          # LED D4 soll leuchten
            LED5.value(LOW)
            LED8.value(LOW)                
            print("Es sollte demnächst gelüftet werden, die Luftqualtiät hat sich verschlechtert.")
            time.sleep(3)                             # Zeitverzögerung von 3 Sekunden

        elif (sgp30.eCO2 < 1000 and sgp30.TVOC < 5):  #Angabe der Sensorwerte in ppm
            LED4.value(LOW)
            LED5.value(LOW)
            LED8.value(HIGH)                          # LED D8 soll leuchten                     
            print("Die Luftqualität ist gut, es besteht kein Grund zu lüften.")
            time.sleep(3)                             #Zeitverzögerung von 3 Sekunden     


except KeyboardInterrupt:    # mit einem KeyboardInterrupt wird die while-Schleife abgebrochen
    LED4.value(LOW)                                   # Pin D4 wird rückgesetzt
    LED5.value(LOW)                                   # Pin D5 wird rückgesetzt
    LED8.value(LOW)                                   # Pin D8 wird rückgesetzt                                  
    pass                                              # Rrogramm wird unterbrochen

