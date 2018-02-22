# This is for serial communication via uart with an arduino

import serial
import time
import port_finder

BAUDRATE = 115200
NUM_LEDS = 240


# Initialize serial communication, 8 data bits, no parity 1 stop bit
ser = serial.Serial('/dev/ttyACM0', BAUDRATE, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
time.sleep(2)

def serial_write(data):
    ser.write(data)   # Encode for python 3

# Read a number of bytes
def serial_read(bytes):
    return ser.read(bytes)

def main():  # This is just a testing function
    # Creating som test_data to send over to arduino
    testdata = bytearray([0, 0, 5]*240)
    testdata2 = bytearray([0, 5, 0]*240)
    testdata3 = bytearray([5, 0, 0]*240)
    testdata5 = bytearray([0, 0, 0]*240)
    testdata4 = bytearray([0, 0, 0]*240)
    #testdata3[719], testdata3[718], testdata3[717] = 5, 5, 5
    testdata4[15] = 255
    testdata5[20] = 255

    while(True):
        serialWrite(testdata)
        time.sleep(0.1)
        serialWrite(testdata2)
        time.sleep(0.1)
        serialWrite(testdata3)
        time.sleep(0.1)

if __name__ == '__main__':
    main()
