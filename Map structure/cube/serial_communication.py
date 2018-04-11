# This is for serial communication via uart with an arduino

import serial
import sys
import serial.tools.list_ports
from constants import BAUDRATE, SIMULATION

class Serial:
    def __init__(self):
        port = _find_arduino_port()
        if(port == None):
            sys.exit("Couldn't find arduino port")
            # Initialize serial communication, 8 data bits, no parity 1 stop bit
        self.ser = serial.Serial(self.port, BAUDRATE, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
        time.sleep(2)

    def _find_arduino_port:
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            if("arduino" in str(port).lower()):
                str(port).split(" -")[0]
        return None

    def write(self, data):
        self.ser.write(data)

    # Included for completenesss, not actually used in our program
    def read(self, num_bytes):
        return self.ser.read(num_bytes)

def main():  # This is just a testing function setting al leds to red
    testdata1 = bytearray([255, 0, 0]*240)
    conn = Serial()
    conn.write(testdata1)

if __name__ == '__main__':
    main()
