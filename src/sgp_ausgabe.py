""" Example for using the SGP30 with CircuitPython and the Adafruit library"""
import time
import board
import busio
import adafruit_sgp30


i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)


("SGP30 serial #", [hex(i) for i in sgp30.serial])

sgp30.iaq_init()
sgp30.set_iaq_baseline(0x986b, 0x8a6a)

elapsed_sec =0

datei = open('textdatei.txt','a')

while elapsed_sec < 7200:
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
    datei.write("%d ppm \t TVOC = %d ppb \n" % (sgp30.eCO2, sgp30.TVOC))
    time.sleep(1)
    elapsed_sec += 1
    #if elapsed_sec > 10:
    #    elapsed_sec = 0
    #    print(
    #        "**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
    #        % (sgp30.baseline_eCO2, sgp30.baseline_TVOC)
    #    )
datei.close()


