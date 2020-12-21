# Ampelsteuerung zur Anzeige der Luftqualität im Raum 
# gemessen werden eCO2 un TVOC

# Alle 3 Sekunden wird die Luftquatlität gemessen

import time
import board
import busio
import mraa
import adafruit_sgp30

from adafruit_blinka.microcontroller.am654 import pin       

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

print("SGP30 serial #", [hex(i) for i in sgp30.serial])

#sgp30.iaq_init()
#sgp30.set_iaq_baseline(0x8973, 0x8AAE)

elapsed_sec = 0

pin.D4.dir(mraa.DIR_OUT)
pin.D5.dir(mraa.DIR_OUT)
pin.D8.dir(mraa.DIR_OUT)

try:
                            # schreibt 1 auf Pin D
    while True: 
        
        if (sgp30.eCO2 < 1000 and sgp30.TVOC < 5):  #Angabe der Sensorwerte in ppm
            pin.D4.write(0)
            pin.D5.write(0)
            pin.D8.write(1)
            print("Die Luftqualität ist gut, es besteht kein Grund zu lüften:")
            time.sleep(3)                           #Zeitverzögerung von 3 Sekunden

        if (sgp30.eCO2 >= 1000 or sgp30.TVOC >= 5):   # Angabe der Sensorwerte in ppm     
            pin.D5.write(0)
            pin.D8.write(0)                         
            pin.D4.write(1)                         # schreibt 1 auf Pin D4
            print("Es sollte demnächst gelüftet werden, die Luftqualtiät hat sich verschlechtert.")
            time.sleep(3)                           # Zeitverzögerung von 3 Sekunden

        if (sgp30.eCO2 > 2000 or sgp30.TVOC > 10):  # Angabe der Sensorwerte in ppm
            pin.D4.write(0)
            pin.D8.write(0)                         
            pin.D5.write(1)                         # schreibt 1 auf Pin D5
            print("Es muss jetzt gelüftet werden, die Luftqualtiät ist schlecht.")
            time.sleep(3)                           # Zeitverzögerung von 3 Sekunden


except KeyboardInterrupt:                           # mit einem KeyboardInterrupt wird die while-Schleife abgebrochen
    pin.D5.write(0)                                 # Pin D5 wird rückgesetzt
    pin.D5.write(0)                                 # Pin D6 wird rückgesetzt
    pin.D8.write(0)                                 # Pin D8 wird rückgesetzt 
    pass                                            # Rrogramm wird unterbrochen

