import pandas as pd
import numpy as np
from colour import Color
import serialTest as st
import time


def plotSpikes(data, N_ROWS, N_LEDS):
    LEDs = bytearray([0, 0, 0]*N_LEDS)
    for i in range(N_ROWS):
        spikes, _ = spikeDetection(data.iloc[i])
        for j in range(len(spikes)):
            if spikes[j] == True:
                temp = bytearray.fromhex(Color("green").get_hex_l())
                for k in range(len(temp)):
                    LEDs[j * 3 + k] = temp[k]
            else:
                temp = bytearray.fromhex(Color("black").get_hex_l())
                for k in range(len(temp)):
                    LEDs[j * 3 + k] = temp[k]
        st.serialWrite(LEDs)
        time.sleep(0.25)


def frequenzyPlot(data, N_ROWS, N_LEDS):
    LEDs = bytearray([0, 0, 0]*N_LEDS)
    n_triggers = np.zeros(60)
    for i in range(N_ROWS):
        spikes, _ = spikeDetection(data.iloc[i])
        print(i)
        for j in range(len(spikes)):
            if spikes[j] == True:
                n_triggers[j] += 1
    colors = genColorGradient("red", "yellow")
    color_groups = n_triggers.max() / len(colors)
    for i in range(len(n_triggers)):
        wannabeSwitchCase(i, n_triggers, colors, color_groups, LEDs)
    st.serialWrite(LEDs)
    time.sleep(0.25)


def intesityPlot(data, N_ROWS, N_LEDS):
    LEDs = bytearray([0, 0, 0]*N_LEDS)
    for i in range(N_ROWS):
        _, values = spikeDetection(data.iloc[i])
        max_value = values.max()
        for j in range(len(values)):
            values[j] -= max_value
        values = values * -1
        colors = genColorGradient("red", "yellow")
        color_groups = values.max() / 10
        for j in range(len(values)):
            wannabeSwitchCase(i, values, colors, color_groups, LEDs)
        st.serialWrite(LEDs)
        time.sleep(0.25)


def genColorGradient(from_color, to_color):
    color1 = Color(from_color)
    return list(color1.range_to(Color(to_color),10))


def wannabeSwitchCase(i, data, color_list, color_groups, LEDs):
    if data[i] <= color_groups:
        temp = bytearray.fromhex(color_list[0].get_hex_l()[1:])
        for j in range(len(temp)):
            LEDs[i * 3 + j] = temp[j]
    elif color_groups < data[i] <= 2 * color_groups:
        temp = bytearray.fromhex(color_list[1].get_hex_l()[1:])
        for j in range(len(temp)):
            LEDs[i * 3 + j] = temp[j]
    elif 2 * color_groups < data[i] <= 3 * color_groups:
        temp = bytearray.fromhex(color_list[2].get_hex_l()[1:])
        for j in range(len(temp)):
            LEDs[i * 3 + j] = temp[j]
    elif 3 * color_groups < data[i] <= 4 * color_groups:
        temp = bytearray.fromhex(color_list[3].get_hex_l()[1:])
        for j in range(len(temp)):
            LEDs[i * 3 + j] = temp[j]
    elif 4 * color_groups < data[i] <= 5 * color_groups:
        temp = bytearray.fromhex(color_list[4].get_hex_l()[1:])
        for j in range(len(temp)):
            LEDs[i * 3 + j] = temp[j]
    elif 5 * color_groups < data[i] <= 6 * color_groups:
        temp = bytearray.fromhex(color_list[5].get_hex_l()[1:])
        for j in range(len(temp)):
            LEDs[i * 3 + j] = temp[j]
    elif 6 * color_groups < data[i] <= 7 * color_groups:
        temp = bytearray.fromhex(color_list[6].get_hex_l()[1:])
        for j in range(len(temp)):
            LEDs[i * 3 + j] = temp[j]
    elif 7 * color_groups < data[i] <= 8 * color_groups:
        temp = bytearray.fromhex(color_list[7].get_hex_l()[1:])
        for j in range(len(temp)):
            LEDs[i * 3 + j] = temp[j]
    elif 8 * color_groups < data[i] <= 9 * color_groups:
        temp = bytearray.fromhex(color_list[8].get_hex_l()[1:])
        for j in range(len(temp)):
            LEDs[i * 3 + j] = temp[j]
    else:
        temp = bytearray.fromhex(color_list[9].get_hex_l()[1:])
        for j in range(len(temp)):
            LEDs[i * 3 + j] = temp[j]


# Returns pd.DataFrame with time [s] as index.
def readCSV(fileName, N_ROWS):
    raw_data = pd.read_csv(fileName, nrows=N_ROWS)
    raw_data.iloc[:,0] = raw_data.iloc[:,0]*10**-6
    raw_data.set_index("TimeStamp [µs]", inplace=True)
    return raw_data


def spikeDetection(data):
    n_colums = data.shape[0]
    spikes = [False]*n_colums
    values = np.zeros(n_colums)
    threshold = -1*10**7

    for i in range(n_colums):
        values[i] = data[i]
        if data[i] <= threshold:
            spikes[i] = True
            #print("Node ID:",i,"Value:",data[i], "[pV]")
    return spikes, values


def main():
    N_ROWS = 10000
    N_LEDS = 240
    fileName = "Data/2017-10-20_MEA2_100000rows_10sec.csv"
    data = readCSV(fileName, N_ROWS)

    # Done
    #plotSpikes(data, N_ROWS, N_LEDS)
    #frequenzyPlot(data, N_ROWS, N_LEDS)
    #intesityPlot(data, N_ROWS, N_LEDS)

    # In development

if __name__ == "__main__":
    main()


    #TODO Generalize plotSpikes
    #TODO Plot cumulative values (using generalization of plotSpikes)
