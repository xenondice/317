# This is for serial communication via uart with an arduino
# python3

import serial
import time
import sys
import port_finder as pf
from led_visualizer import *
from constants import BAUDRATE, SIMULATION

# Initialize serial communication, 8 data bits, no parity 1 stop bit
port = pf.find_arduino_port()
#if(port == None):
#    sys.exit("Couldn't find arduino port")

ser = serial.Serial(port, BAUDRATE, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
#vis_init()
time.sleep(2)

def serial_write(data):
    if not SIMULATION:
        ser.write(data)
    else:
        vis_update(data)
    

# Read a number of bytes
def serial_read(bytes):
    return ser.read(bytes)

def main():  # This is just a testing function
    # Creating som test_data to send over to arduino
    testdata = bytearray([0, 0, 255]*240)
    testdata2 = bytearray([0, 255, 0]*240)
    testdata3 = bytearray([255, 0, 0]*240)
    testdata5 = bytearray([0, 0, 0]*240)
    testdata4 = bytearray([0, 0, 0]*240)
    #testdata3[719], testdata3[718], testdata3[717] = 5, 5, 5
    testdata4[15] = 255
    testdata5[20] = 255
    while(True):
        serial_write(testdata)
        time.sleep(0.1)
        serial_write(testdata2)
        time.sleep(0.1)
        serial_write(testdata3)
        time.sleep(0.1)

if __name__ == '__main__':
    main()
