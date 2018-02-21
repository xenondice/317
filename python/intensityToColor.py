# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:13:44 2018

@author: Andreas
"""

from colour import Color
import serialTest as st
import time

intensity[60]

LEDs = bytearray([0, 0, 0]*NUM_LEDS)

def genColorGradient(from_color, to_color):
    color1 = Color(from_color)
    return list(color1.range_to(Color(to_color),10))

def dataToColor(intensity, color1, color2):
    colors = genColorGratient(color1, color2)
    hexIntensity[60]
    for i in range(len(intensity)):
        hexIntensity[i] = colors[intensity[i]].get_hex_l()   
    return hexIntensity