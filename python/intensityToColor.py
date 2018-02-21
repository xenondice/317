# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:13:44 2018

@author: Andreas
"""

from colour import Color
from random import randint

intensity = [0]*60

# LEDs = bytearray([0, 0, 0]*NUM_LEDS)

def genColorGradient(from_color, to_color):
    color1 = Color(from_color)
    return list(color1.range_to(Color(to_color),10))

def dataToColor(intensity, color1, color2):
    colors = genColorGradient(color1, color2)
    hexIntensity = [0]*60
    for i in range(len(intensity)):
        hexIntensity[i] = colors[intensity[i]].get_hex_l()
        print(hexIntensity[i])
    return hexIntensity

# def fromHexToByte: to be continued
    

def main():
    for i in range(len(intensity)):
        intensity[i] = randint(0,9)
    dataToColor(intensity, Color("red"), Color("yellow"))
    
    
    
if __name__ == '__main__':
    main()