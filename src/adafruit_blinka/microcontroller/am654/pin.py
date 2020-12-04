
"Broadcom AM654 pin names"

#import RPi.GPIO as GPIO
import mraa
import time

#mraa.Gpio.setmode(mraa.Gpio.BCM)  #Use BCM pins D4 = GPIO #4
#mraa.Gpio.setwarnings(False) #shh!



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

    def init(self, mode=IN, pull=None):
        "Initialise the Pin"
        if mode is not None:
            if mode == self.IN:
                self._mode = self.IN
                mraa.Gpio.setup(self.id, mraa.Gpio.write())
                self.dir(mraa.DIR_IN)
            if mode == self.OUT:
                self._mode = slef.OUT
                mraa.Gpio.setup(self.id, mraa.Gpio.read())
                self.dir(mraa.DIR_OUT)
            elif mode == self.OUT:
                self._mode = self.OUT
                mraa.Gpio.setup(self.id, mraa.Gpio.OUT)
            else: 
                raise RuntimeError("Invalid mode for pin: %s" % self.id)
        if pull is not None:
            if self._mode != self.IN:
                raise RuntimeError("Cannot set pull resistor on output")
            if pull == self.PULL_UP:
                mraa.Gpio.setup(self.id, mraa.Gpio.IN, pull_up_down=mraa.Gpio.PUD_UP)
            elif pull == self.PULL_DOWN:
                mraa.Gpio.setup(self.id, mraa.Gpio.IN, pull_up_down=mraa.Gpio.PUD_DOWN)
            else:
                raise RuntimeError("Invalid pull for pin: %s" % self.id)

        def value(self, val=None):
            "Set or return the Pin Value"
            if val is not None:
                if val == self.LOW:
                    self._value = val
                    mraa.Gpio.output(self.id, val)
                elif val == self.HIGH:
                    self._value = val
                    mraa.Gpio.output(self.id, val)
                else: 
                    raise RuntimeError("Invalid value for pin")
                return None
            return mraa.Gpio.input(self.id)


I2C_SCL = Pin(19)
I2C_SDA = Pin(18)

#Digital Pins

D4 = mraa.Gpio(4) #Digital PIN 4
D4.dir(mraa.DIR_OUT)

#    D4.write(1)
#    time.sleep(1)
#    D4.write(0)
#    time.sleep(1)




D5 = mraa.Gpio(5) #Digital PIN 5
D5.dir(mraa.DIR_OUT)

D5.write(1)
time.sleep(1)
D5.write(0)
time.sleep(1)




D8 = mraa.Gpio(8) #Digital PIN 8
D8.dir(mraa.DIR_OUT)

D8.write(1)
time.sleep(1)
D8.write(0)
time.sleep(1   )




D9 = mraa.Gpio(9) #Digital PIN 9
D9.dir(mraa.DIR_OUT)

D9.write(1)
time.sleep(1)
D9.write(0)
time.sleep(1)



#Analoge Pins

A0 = mraa.Aio(0) #Analog PIN 0
value_A0 = A0.read()
#print (value_A0)

A1 = mraa.Aio(1) #Analog PIN 1
value_A1 = A1.read()
#print (value_A1)

A2 = mraa.Aio(2) #Analog PIN 2
value_A2 = A2.read()
#print (value_A2)

A3 = mraa.Aio(3) #Analog PIN 3
value_A3 = A3.read()
#print (value_A3)


#SPI
#ordered as spiId, sckId, mosiID, misoID


#URAT
# ordered as uartID, txID, rxId


#I2C
i2cPorts = (4, I2C_SCL, I2C_SDA), #erste Ziffer ist Bus Nummer



