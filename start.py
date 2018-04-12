from python.constants import *
from python.led_visualizer import *
from colour import Color
from random import randint
from math import pi
import time
import websocket
import json
import sys
import python.port_finder as pf
import serial

ser = None

def setup():
    global ser
    if SIMULATION:
        visualizer_init()
    else:
        port = pf.find_arduino_port()
        if(port == None):
            sys.exit("Couldn't find arduino port")

        ser = serial.Serial(port, BAUDRATE, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
        
def update(colors):
    if SIMULATION:
        visualizer_update(colors)
    else:
        ser.write(colors)

def running():
    if SIMULATION:
        return visualizer_running()
    else:
        return False

def program_smily(led_colors):
    if MODEL['name'] != 'cube':
        print("Model not supported by current program")
        exit()
    
    for x in range(10):
        for y in range(5):
            top_id = MODEL['led-groups']['top'][y][x]
            if top_id != -1:
                led_colors[top_id * 3] = 0
                led_colors[top_id * 3 + 1] = 0
                led_colors[top_id * 3 + 2] = 0
    n = 40
    for x in range(40):
        rad = (x/39)*2*pi
        color = Color(hue=(x/39), saturation=1, luminance=0.5)
        ids = [
            [2, 0],
            [2, 1],
            [2, 2],
            [6, 0],
            [6, 1],
            [6, 2],
            [0, 3],
            [1, 4],
            [2, 4],
            [3, 4],
            [4, 4],
            [5, 4],
            [6, 4],
            [7, 4],
            [8, 3]
        ]
        for led in ids:
            top_id = MODEL['led-groups']['top'][led[1]][led[0]]
            if top_id != -1:
                led_colors[top_id * 3] = int(color.get_red()*255)
                led_colors[top_id * 3 + 1] = int(color.get_green()*255)
                led_colors[top_id * 3 + 2] = int(color.get_blue()*255)
        for t in range(n):
            prev = (x-t) % 40
            falloff = (n-t-1)/(n-1)
            rad = (prev/39)
            color = Color(hue=rad, saturation=1, luminance=0.5)
            for y in range(5):
                x_off = prev
                side = 'north'
                if prev < 10:
                    pass
                elif prev < 20:
                    x_off -= 10
                    side = 'west'
                elif prev < 30:
                    x_off -= 20
                    side = 'south'
                else:
                    x_off -= 30
                    side = 'east'
                led_id = MODEL['led-groups'][side][y][x_off]
                if led_id != -1:
                    led_colors[led_id*3] = int(color.get_red()*255*falloff)
                    led_colors[led_id*3+1] = int(color.get_green()*255*falloff)
                    led_colors[led_id*3+2] = int(color.get_blue()*255*falloff)
        update(led_colors)
        time.sleep(1/60)

def program_websocket(led_colors):
    websocket.enableTrace(True)
    def on_close(ws):
        print("Connection closed")
        exit()
    def on_error(ws, error):
        print("Connection error: {}".format(error))
        exit()
    def on_open(ws):
        print("Connection established")
    def on_message(ws, message):
        leds = json.loads(message)
        for i in range(len(leds)):
            val = leds[i]
            if val > 255:
                val = 255
            led_colors[i*3] = val
            led_colors[i*3+1] = val
            led_colors[i*3+2] = val
        update(led_colors)
    ws = websocket.WebSocketApp("ws://127.0.0.1:6780/data/1000/",
    on_message = on_message,
    on_error = on_error,
    on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

def program_snake(led_colors):
    for i in range(MODEL['led-quantity']):
        n = 200
        for k in range(n):
            prev = (i - k) % MODEL['led-quantity']
            falloff = (n-k - 1)/n
            for j in range(3):
                led_colors[prev*3+j] = randint(0, int(255*falloff)) + int(255*(1-falloff))
        update(led_colors)
        time.sleep(1.0/60)

if __name__ == "__main__":
    """ TODO
    Able to specify output source (virtual or usb),
    input source (server ip, file, nothing),
    program/filter (heatmap, random, smile, etc),
    refreshrate (100ms),
    model (cube, small-cube, dome, error message if imcompatible filter),
    type of data from neurons (average voltage, numer of spikes)
    start.py --out virtual --in "127.0.0.1" --fps 10 --filter heatmap --model cube --datatype spikes
    Blink red if no connection
    """
    
    setup()

    led_colors = bytearray([0] * (3*MODEL['led-quantity']))
    
    while running():
        if PROGRAM == 'snake':
            program_snake(led_colors)
        elif PROGRAM == 'smily':
            program_smily(led_colors)
        elif PROGRAM == 'websocket':
            program_websocket(led_colors)
            break