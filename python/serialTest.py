# This is for serial communication via uart with an arduino

import serial
import time

BAUDRATE = 57600


ser = serial.Serial('/dev/ttyACM0', BAUDRATE)

def serialInit(baudrate):
    #ser = serial.Serial('/dev/ttyACM0', BAUDRATE)
    return 0

def serialWrite(data):
    ser.write(data)   # Encode for python 3
"""
def arrayToString(array):
    output = ""
    for value in array:
        output += value + ' '
    output += '\n'
    return output
"""

def serialTest():
    # Creating som test_data to send over to arduino
    testdata = bytearray([255, 0, 0]*240)
    testdata2 = bytearray([0, 255, 0]*240)
    testdata3 = bytearray([0, 0, 0]*240)
    testdata3[0], testdata3[1], testdata3[2] = 150, 160, 145
    #inputToArduino = arrayToString(testdata)
    #inputToArduino2 = arrayToString(testdata2)
    #inputToArduino3 = arrayToString(testdata3)

    serialInit(BAUDRATE)
    time.sleep(1)
    while(True):
        ser.write(testdata)
        time.sleep(5)
        ser.write(testdata2)
        time.sleep(5)
        ser.write(testdata3)
        time.sleep(5)
    print("heifahif")
serialTest();
