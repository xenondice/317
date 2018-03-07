import pandas as pd
import numpy as np
import intensity_to_color as itc
import serial_communication
import time
from led_visualizer import *


# Returns pd.DataFrame with time [s] as index.
def read_csv(file_name, N_ROWS):
    raw_data = pd.read_csv(file_name, nrows=N_ROWS)
    raw_data.iloc[:, 0] = raw_data.iloc[:, 0]*10**-6
    raw_data.set_index("TimeStamp [µs]", inplace=True)
    return raw_data


def spike_detection(data):
    n_columns = data.shape[0]
    spikes = [False]*n_columns
    volt = np.zeros(n_columns)
    threshold = -1*10**7

    for i in range(n_columns):
        volt[i] = data[i]
        if data[i] <= threshold:
            spikes[i] = True
            # print("Node ID:",i,"Value:",data[i], "[pV]")
    return spikes, volt


def spikes_plot(data, N_ROWS):
    for i in range(N_ROWS):
        spikes, _ = spike_detection(data.iloc[i])
        leds = np.zeros(60)
        for j in range(len(leds)):
            if not spikes[j]:
                leds[j] = 0
            else:
                leds[j] = 9
        print(leds)
        itc.intensity_to_bytearray_write(leds, 'red', 'green')


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
    #print(leds)
    itc.intensity_to_bytearray_write(leds, 'red', 'green')


def intensity_plot(data, N_ROWS):
    for i in range(N_ROWS):
        _, volt = spike_detection(data.iloc[i])
        max_value = volt.max()
        for j in range(len(volt)):
            volt[j] -= max_value
        volt = volt * -1
        volt_per_group = volt.max() / 10
        leds = np.zeros(60)
        for j in range(len(volt)):
            leds[j] = color_grouping(j, volt, volt_per_group)
        #print(leds)
        itc.intensity_to_bytearray_write(leds, 'blue', 'red')
        time.sleep(0.0001)


def color_grouping(index, values, value_per_group):
    if values[index] <= value_per_group:
        return 0
    elif value_per_group < values[index] <= 2 * value_per_group:
        return 1
    elif 2*value_per_group < values[index] <= 3*value_per_group:
        return 2
    elif 3 * value_per_group < values[index] <= 4 * value_per_group:
        return 3
    elif 4 * value_per_group < values[index] <= 5 * value_per_group:
        return 4
    elif 5 * value_per_group < values[index] <= 6 * value_per_group:
        return 5
    elif 6 * value_per_group < values[index] <= 7 * value_per_group:
        return 6
    elif 7 * value_per_group < values[index] <= 8 * value_per_group:
        return 7
    elif 8 * value_per_group < values[index] <= 9 * value_per_group:
        return 8
    else:
        return 9


def main():
    vis_init()
    N_ROWS = 1000
    file_name = "Data/2017-10-20_MEA2_100000rows_10sec.csv"
    data = read_csv(file_name, N_ROWS)

    # spikes_plot(data, N_ROWS)
    # frequency_plot(data, N_ROWS)
    intensity_plot(data, N_ROWS)


if __name__ == "__main__":
    main()
