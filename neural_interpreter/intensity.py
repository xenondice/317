import system.settings as settings
import sys
import neural_interpreter.support_functions.data_to_color as d2c

class Intensity:
    def __init__(self):
        if settings.NEURAL_DATA_TYPE != 'intensity' and settings.NEURAL_SOURCE != 'file':
            sys.exit('This interpreter is not available in this mode. Use --file <location> and --datatype intensity')

    def render(self, input_data, output_data):
        max_value = input_data.max()
        for j in range(len(volt)):
            volt[j] -= max_value
        volt = volt * -1
        volt_per_group = volt.max() / 10
        leds = np.zeros(60)
        for j in range(len(volt)):
            leds[j] = d2c.color_grouping(j, volt, volt_per_group)

if __name__ == '__main__':
    pass