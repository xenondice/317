from led_visualizer import *
from constants import *
from colour import Color
from random import randint
from math import pi
import time

def setup():
    if SIMULATION:
        visualizer_init()
    else:
        print("Non virtual not supported yet")
        exit()

def update(colors):
    if SIMULATION:
        visualizer_update(colors)
    else:
        pass

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
    setup()

    led_colors = [0] * (3*MODEL['led-quantity'])
    
    while running():
        if PROGRAM == 'snake':
            program_snake(led_colors)
        elif PROGRAM == 'smily':
            program_smily(led_colors)