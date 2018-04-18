import statistics
import data_to_color as d2c

# Takes in array of size 60 with frequences
class frequency_plot:
    def __init__(self):
        self.high = 0
        self.low = 0
        self.initialized = False

    def update(self, input_data, output_data):
        intensities = [0]*60
        median = statistics.median(sorted(updatedata))
        max_frequency = max(updatedata)
        min_frequency = min(updatedata)
        if max_frequency >= 4* median:   ## Done to avoid very dominant nodes maybe implement better solution
            max_frequency = 2*median    #TODO better?
        if self.initialized == False:
            self.high = max_frequency
            self.low = min_frequency
            self.initialized = True
        else:
            self.high = self.high*0.9 + 0.1*max_frequency
            self.low = self.low*0.9 + 0.1*min_frequency
        for index in range(len(updatedata)):
            intens = int((updatedata[index]-self.low)/(self.high - self.low)*10)
            intens = min(9, intens)
            intens = max(0, intens)
            intensities[index] = intens
        d2c.data_to_bytearray(intensities, output_data)
