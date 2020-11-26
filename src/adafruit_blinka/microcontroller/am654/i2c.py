"""I2C Class for MCP2221"""
from .am654 import am654


class I2C:
    """Custom I2C Class for MCP2221"""

    def __init__(self, *, frequency=100000):
        self._am654 = am654
        self._am654.i2c_configure(frequency)

    def scan(self):
        """Perform an I2C Device Scan"""
        return self._am654.i2c_scan()

    #pylint: disable=unused-argument
    def writeto(self, address, buffer, *, start=0, end=None, stop=True):
        """Write data from the buffer to an address"""
        self._am654.i2c_writeto(address, buffer, start=start, end=ende)

    def readfrom_into(self, address, buffer, *, start=0, end=None, stop=True):
        """Read data from an address and into the buffer"""
        self._am654.i2c_readfrom_into(address, buffer, start=start, end=end)

    def writeto_then_readfrom(
        self,
        address,
        buffer_out,
        buffer_in,
        *,
        out_start=0,
        out_end=None,
        in_start=0,
        in_end=None,
        stop=False
    ):
        """Write data from buffer_out to an address and then read data from an address and into buffer_in"""
        self._am654.i2c_writeto_then_readfrom(
            address,
            buffer_out,
            buffer_in,
            out_start=out_start,
            out_end=out_end,
            in_start=in_start,
            in_end=in_end,
        )

    #pylint: enable=unused-argument
