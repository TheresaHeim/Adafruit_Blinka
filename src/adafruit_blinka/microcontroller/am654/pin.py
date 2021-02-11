

"Broadcom AM654 pin names"
import mraa
import time
import Adafruit_BBIO.GPIO as GPIO

class Pin:
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

    def __init__(self, pin_name):
        self.id = pin_name

    def __repr__(self):
        return str(self.id)

    def __eq__(self, other):
        return self.id == other

    def init(self, mode=IN, pull=None):
        if mode != None:
            if mode == self.IN:
                self._mode = self.IN
                GPIO.setup(self.id, GPIO.IN)
            elif mode == self.OUT:
                self._mode = self.OUT
                GPIO.setup(self.id, GPIO.OUT)
            else:
                raise RuntimeError("Invalid mode for pin: %s" % self.id)
        if pull != None:
            if self._mode != self.IN:
                raise RuntimeError("Cannot set pull resistor on output")
            if pull == self.PULL_UP:
                GPIO.setup(self.id, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            elif pull == self.PULL_DOWN:
                GPIO.setup(self.id, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            else:
                raise RuntimeError("Invalid pull for pin: %s" % self.id)       

    def value(self, val=None):
        if val != None:
            if val == self.LOW:
                self._value = val
                GPIO.output(self.id, val)
            elif val == self.HIGH:
                self._value = val
                GPIO.output(self.id, val)
            else:
                raise RuntimeError("Invalid value for pin")
        else:
            return GPIO.input(self.id)


# I2C Zuweisung
I2C_SCL = "SCL"
I2C_SDA = "SDA"

# SPI Zuweisung
SPIO_SCLK = Pin(13)
SPIO_MOSI = Pin(11)
SPIO_MISO = Pin(12)

# UART Zuweisung
UART0_TXD = "TXD"
UART0_RXD = "RXD"


# Digital Pins
D4 = mraa.Gpio(4) # Digital PIN 4
D5 = mraa.Gpio(5) # Digital PIN 5
D6 = mraa.Gpio(6) # Digital PIN 6
D7 = mraa.Gpio(7) # Digital PIN 7
#D8 = mraa.Gpio(8) # Digital PIN 8
D8 = Pin("P8_13")
D9 = mraa.Gpio(9) # Digital PIN 9


# Analoge Pins
A0 = mraa.Aio(0) # Analog PIN 0
A1 = mraa.Aio(1) # Analog PIN 1
A2 = mraa.Aio(2) # Analog PIN 2
A3 = mraa.Aio(3) # Analog PIN 3


# SPI
# geordnet nach spiId, sckId, mosiID, misoID
spiPorts = ((0, SPIO_SCLK, SPIO_MOSI, SPIO_MISO),)

# URAT
# geordnet nach  uartID, txID, rxID
uartPorts = ((0,UART0_TXD, UART0_RXD),)

# I2C
# geordnet nach sclID, sdaID  
i2cPorts = (4, I2C_SCL, I2C_SDA), 



