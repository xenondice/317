# This is for serial communication via uart with an arduino

import serial
import sys
import time
import serial.tools.list_ports
from system.settings import

class SerialInterface:
    def __init__(self):
        port = self._find_arduino_port()
        if port == None:
            sys.exit("Couldn't find arduino port")
         # Initialize serial communication, 8 data bits, no parity 1 stop bit
        self.ser = serial.Serial(port, SERIAL_BAUD_RATE, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
        time.sleep(2)

    def _find_arduino_port(self):
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            if ("arduino" in str(port).lower()):
                return  str(port).split(" -")[0]
            else:
                return None

    def refresh(self, data):
        self.ser.write(data)

    # Included for completenesss, not actually used in our program
    def read(self, num_bytes):
        return self.ser.read(num_bytes)

def main():  # This is just a testing function setting all leds to red
    testdata1 = bytearray([255, 0, 0]*240)
    conn = SerialInterface()
    conn.refresh(testdata1)

if __name__ == '__main__':
    main()
