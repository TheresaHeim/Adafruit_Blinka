import time
import board
import busio
import digitalio
import adafruit_max31855
import mraa
import adafruit_blinka.microcontroller.am654.pin

spi = busio.SPI(board.SCLK, MOSI=board.MOSI, MISO=board.MISO)
cs = adafruit_blinka.microcontroller.am654.pin.D6
 
max31855 = adafruit_max31855.MAX31855(spi, cs)
while True:
    tempC = max31855.temperature
    tempF = tempC * 9 / 5 + 32
    print("Temperature: {} C {} F ".format(tempC, tempF))
    time.sleep(2.0)
