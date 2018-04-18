#import system.settings as settings
import random

class RandomMode:
    def __init__(self):

    def update(self, input_data, output_data):
        for i in range(240):
            for j in range(3):
                output_data[i*3 + j] = random.randint(0, 255)

