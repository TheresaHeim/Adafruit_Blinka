
"Broadcom AM654 pin names"

import RPi.GPIO as GPIO
import mraa
import time

GPIO.setmode(GPIO.BCM)  #Use BCM pins D4 = GPIO #4
GPIO.setwarnings(False) #shh!


class Pin: 
    "Pins dont exist in CPython so ... lets make our own!"

    IN = 0
    OUT = 1
    LOW = 0
    HIGH = 1
    PULL_NONE = 0
    PULL_UP = 1
    PULL_DOWN = 2

    id = None
    _value = LOW
    _mode = IN

    def __init__(self, bcm_number):

        self.id = bcm_number

    def __repr__(self):
        return str(self.id)

    def __eq__(self, other):
        return self.id == other

    def init(self, mode=write, pull=None):
        "Initialise the Pin"
        if mode is not None:
            if mode == self.write:
                self._mode = self.write()
                GPIO.setup(self.id, GPIO.write())
            if mode == self.read:
                self._mode = slef.read()
                GPIO.setup(self.id, GPIO.read())
            elif mode == self.OUT:
                self._mode = self.OUT
                GPIO.setup(self.id, GPIO.OUT)
            else: 
                raise RuntimeError("Invalid mode for pin: %s" % self.id)
        if pull is not None:
            if self._mode != self.IN:
                raise RuntimeError("Cannot set pull resistor on output")
            if pull == self.PULL_UP:
                GPIO.setup(self.id, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            elif pull == self.PULL_DOWN:
                GPIO.setup(self.id, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            else:
                raise RuntimeError("Invalid pull for pin: %s" % self.id)

        def value(self, val=None):
            "Set or return the Pin Value"
            if val is not None:
                if val == self.LOW:
                    self._value = val
                    GPIO.output(self.id, val)
                elif val == self.HIGH:
                    self._value = val
                    GPIO.output(self.id, val)
                else: 
                    raise RuntimeError("Invalid value for pin")
                return None
            return GPIO.input(self.id)


#Digital Pins

D4 = mrra.GPIO(4) #Digital PIN 4

D5 = mraa.GPIO(5) #Digital PIN 5

D6 = mraa.GPIO(6) #Digital PIN 6

D7 = mraa.GPIO(7) #Digital PIN 7

D8 = mraa.GPIO(8) #Digital PIN 8

D9 = mraa.GPIO(9) #Digital PIN 9

#Analoge Pins

A0 = mraa.Aio(0) #Analog PIN 0

A1 = mraa.Aio(1) #Analog PIN 1

A2 = mraa.Aio(2) #Analog PIN 2

A3 = mraa.Aio(3) #Analog PIN 3

#SPI
#ordered as spiId, sckId, mosiID, misoID



#URAT
# ordered as uartID, txID, rxId



#I2C
i2cPorts = ( 
        4, "A5", "A6"), #erste Ziffer ist Bus Nummer
)
