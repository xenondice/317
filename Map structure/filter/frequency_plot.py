import statistics
import data_to_color as d2c



# TODO: Started but not finished
'''
def frequency_plot(data, N_ROWS):
    n_triggers = np.zeros(60)
    for i in range(N_ROWS):
        spikes, _ = spike_detection(data.iloc[i])
        for j in range(len(spikes)):
            if spikes[j]:
                n_triggers[j] += 1
    spikes_per_group = n_triggers.max() / 10
    leds = np.zeros(60)
    for i in range(len(leds)):
        leds[i] = color_grouping(i, n_triggers, spikes_per_group)
    # print(leds)
    d2c.data_to_bytearray_write(leds, settings)
'''

# Takes in array of size 60 with frequences
class Frequency_plot:
    def __init__(self, datatype, output, settings):
        self.datatype = datatype
        self.output = output
        self.settings = settings
        self.high = 0
        self.low = 0
        self.initialized = False

    def update(self, updatedata):
        intensities = [0]*60
        median = statistics.median(sorted(updatedata))
        max_frequency = max(updatedata)
        min_frequency = min(updatedata)
        if max_frequency >= 4* median:   ## Done to avoid very dominant nodes maybe implement better solution
            max_frequency = 3*median    #TODO more elegant?
        if self.initialized == False:
            self.high = max_frequency
            self.low = min_frequency
            self.initialized = True
        else:
            self.high = self.high*0.95 + 0.05*max_frequency
            self.low = self.low*0.95 +0.05*min_frequency
        for index in range(len(updatedata)):
            intens = int((updatedata[index]-self.low)/(self.high - self.low)*10)
            intens = min(9, intens)
            intens = max(0, intens)
            intensities[index] = intens
        bytes = d2c.data_to_bytearray(intensities, self.settings)
        return bytes
