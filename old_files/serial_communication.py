# This is for serial communication via uart with an arduino
# python3

import serial
import time
import sys
import port_finder as pf
import system.settings as settings
from constants import BAUDRATE, SIMULATION

# Initialize serial communication, 8 data bits, no parity 1 stop bit
port = pf.find_arduino_port()
if(port == None):
    sys.exit("Couldn't find arduino port")

ser = serial.Serial(port, settings.SERIAL_BAUD_RATE, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
time.sleep(2)

def serial_write(data):
    if not SIMULATION:
        ser.write(data)
    else:
        pass

# Read a number of bytes
def serial_read(bytes):
    if not SIMULATION:
        return ser.read(bytes)

def main():  # This is just a testing function
    testdata1 = bytearray([255, 0, 0]*240)
    testdata2 = bytearray([0, 255, 0]*240)
    testdata3 = bytearray([0, 0, 255]*240)
    testdata4 = bytearray([255, 255, 255]*240)
    serial_write(testdata4)
    '''
    while(True):
        serialWrite(testdata1)
        time.sleep(0.3)
        serialWrite(testdata2)
        time.sleep(0.3)
        serialWrite(testdata3)
        time.sleep(0.3)
    '''

if __name__ == '__main__':
    main()