from colour import Color
from random import randint
NUM_LEDS = 240
import serial_communication as serial

def gen_color_gradient(from_color, to_color):
    color1 = Color(from_color)
    return list(color1.range_to(Color(to_color),10))

def intensity_to_hex(intensity, from_color, to_color):
    colors = gen_color_gradient(from_color, to_color)
    hexIntensity = [0]*60
    for i in range(len(intensity)):
        hexIntensity[i] = colors[int(intensity[i])].get_hex_l()
    return hexIntensity

def intensity_to_bytearray_write(intensity, from_color, to_color):
    hexarray = intensity_to_hex(intensity, from_color, to_color)
    num_leds_cluster = int(NUM_LEDS/60)
    byteArr = bytearray([0, 0, 0]*NUM_LEDS)
    for i in range(len(hexarray)):
        for j in range(num_leds_cluster):
            index = i*3*num_leds_cluster+3*j
            byteArr[index:index+3] = bytearray.fromhex(hexarray[i][1:])
    serial.serial_write(byteArr)

def main():
    pass
    '''
    intensity = [0]*60
    for i in range(len(intensity)):
        intensity[i] = randint(0,9)
        dataToColor(intensity, Color("red"), Color("yellow"))
    '''

if __name__ == '__main__':
    main()