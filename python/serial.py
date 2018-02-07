# This is for serial communication via uart with an arduino

import serial
import time

BAUDRATE = 9600


ser = None

def serialInit(baudrate):
    serial.Serial('/dev/ttyACM0', baudrate)

def serialWrite(data):
    ser.write(data.encode())   # Encode for python 3

def arrayToString(array):
    output = ""
    for value in array:
        output += value + ' '
    output += '\n'
    return output

def serialTest():
    # Creating som test_data to send over to arduino
    testdata = ['255', '0', '0']*240
    testdata2 = ['0', '255', '0']*240
    testdata3 = ['0', '0', '0']*240
    testdata3[0], testdata3[1], testdata3[2] = '150', '160', '145'
    inputToArduino = arrayToString(testdata)
    inputToArduino2 = arrayToString(testdata2)
    inputToArduino3 = arrayToString(testdata3)
    
    init(BAUDRATE)
    time.sleep(1)
    while(True):
        write(inputToArduino)
        time.sleep(5)
        write(inputToArduino2)
        time.sleep(5)
        write(inputToArduino3)
        time.sleep(5)

serialTest();
