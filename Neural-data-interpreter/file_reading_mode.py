import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from colour import Color

def plotSpikes(data, N_ROWS):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(N_ROWS):
        spikes, _ = spikeDetection(data.iloc[i])
        setupFigureFrame(spikes, ax, "green", "none")
        plt.title("Iteration: " + str(i) + "\nTime: " + str(i/10000) +"s")
        plt.draw()
        plt.pause(0.001)
        ax.clear()


def frequenzyPlot(data, N_ROWS):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    n_triggers = np.zeros(60)
    for i in range(N_ROWS):
        spikes, _ = spikeDetection(data.iloc[i])
        print(i)
        for j in range(len(spikes)):
            if spikes[j] == True:
                n_triggers[j] += 1
    print(n_triggers)
    colors = genColorGradient("red", "yellow")
    color_groups = n_triggers.max() / len(colors)
    x_pos = 0.6
    y_pos = 0.6
    x_size = 0.8
    y_size = 0.8
    j = 0
    for i in range(len(n_triggers)):
        if n_triggers[i] <= color_groups:
            genPatches(ax, x_pos, y_pos, x_size, y_size, str(colors[0].get_hex_l()))
        elif color_groups < n_triggers[i] <= 2*color_groups:
            genPatches(ax, x_pos, y_pos, x_size, y_size, str(colors[1].get_hex_l()))
        elif 2*color_groups < n_triggers[i] <= 3*color_groups:
            genPatches(ax, x_pos, y_pos, x_size, y_size, str(colors[2].get_hex_l()))
        elif 3*color_groups < n_triggers[i] <= 4*color_groups:
            genPatches(ax, x_pos, y_pos, x_size, y_size, str(colors[3].get_hex_l()))
        elif 4*color_groups < n_triggers[i] <= 5*color_groups:
            genPatches(ax, x_pos, y_pos, x_size, y_size, str(colors[4].get_hex_l()))
        elif 5*color_groups < n_triggers[i] <= 6*color_groups:
            genPatches(ax, x_pos, y_pos, x_size, y_size, str(colors[5].get_hex_l()))
        elif 6*color_groups < n_triggers[i] <= 7*color_groups:
            genPatches(ax, x_pos, y_pos, x_size, y_size, str(colors[6].get_hex_l()))
        elif 7*color_groups < n_triggers[i] <= 8*color_groups:
            genPatches(ax, x_pos, y_pos, x_size, y_size, str(colors[7].get_hex_l()))
        elif 8*color_groups < n_triggers[i] <= 9*color_groups:
            genPatches(ax, x_pos, y_pos, x_size, y_size, str(colors[8].get_hex_l()))
        else:
            genPatches(ax, x_pos, y_pos, x_size, y_size, str(colors[9].get_hex_l()))

        if j == 9:
            y_pos += y_size + 0.2
            x_pos = 0.6
            j = 0
        else:
            x_pos += x_size + 0.2
            j += 1
    plt.ylim([0, 7])
    plt.xlim([0, 11])
    plt.plot()
    plt.show()


def intesityPlot(data, N_ROWS):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(N_ROWS):
        _, values = spikeDetection(data.iloc[i])
        max_value = values.max()
        for j in range(len(values)):
            values[j] -= max_value
        values = values * -1
        colors = genColorGradient("red", "yellow")
        color_groups = values.max() / 10
        x_pos = 0.6
        y_pos = 0.6
        x_size = 0.8
        y_size = 0.8
        k = 0
        print(colors[0].get_hex_l())
        for j in range(len(values)):
            if values[j] <= color_groups:
                genPatches(ax, x_pos, y_pos, x_size, y_size, colors[0].get_hex_l())
            elif color_groups < values[j] <= 2 * color_groups:
                genPatches(ax, x_pos, y_pos, x_size, y_size, colors[1].get_hex_l())
            elif 2 * color_groups < values[j] <= 3 * color_groups:
                genPatches(ax, x_pos, y_pos, x_size, y_size, colors[2].get_hex_l())
            elif 3 * color_groups < values[j] <= 4 * color_groups:
                genPatches(ax, x_pos, y_pos, x_size, y_size, colors[3].get_hex_l())
            elif 4 * color_groups < values[j] <= 5 * color_groups:
                genPatches(ax, x_pos, y_pos, x_size, y_size, colors[4].get_hex_l())
            elif 5 * color_groups < values[j] <= 6 * color_groups:
                genPatches(ax, x_pos, y_pos, x_size, y_size, colors[5].get_hex_l())
            elif 6 * color_groups < values[j] <= 7 * color_groups:
                genPatches(ax, x_pos, y_pos, x_size, y_size, colors[6].get_hex_l())
            elif 7 * color_groups < values[j] <= 8 * color_groups:
                genPatches(ax, x_pos, y_pos, x_size, y_size, colors[7].get_hex_l())
            elif 8 * color_groups < values[j] <= 9 * color_groups:
                genPatches(ax, x_pos, y_pos, x_size, y_size, colors[8].get_hex_l())
            else:
                genPatches(ax, x_pos, y_pos, x_size, y_size, colors[9].get_hex_l())
            if k == 9:
                y_pos += y_size + 0.2
                x_pos = 0.6
                k = 0
            else:
                x_pos += x_size + 0.2
                k += 1
        plt.title("Iteration: " + str(i) + "\nTime: " + str(i/10000) +"s")
        plt.ylim([0, 7])
        plt.xlim([0, 11])
        plt.draw()
        plt.pause(0.001)
        ax.clear()


def genColorGradient(from_color, to_color):
    color1 = Color(from_color)
    return list(color1.range_to(Color(to_color),10))



def setupFigureFrame(LED, ax, true_color, false_color):
    '''
    Input:  LED         (1x60 matrix containing boolean values)
            ax          (axis of a subplot)
            true_color  (color of the patch for True value)
            false color (color of the patch for False value)
    '''
    x_pos = 0.6
    y_pos = 0.6
    x_size = 0.8
    y_size = 0.8
    j = 0
    for diode in LED:
        if diode == True:
            genPatches(ax, x_pos, y_pos, x_size, y_size, true_color)
        else:
            genPatches(ax, x_pos, y_pos, x_size, y_size, false_color)
        if j == 9:
            y_pos += y_size + 0.2
            x_pos = 0.6
            j = 0
        else:
            x_pos += x_size + 0.2
            j += 1
    plt.ylim([0, 7])
    plt.xlim([0, 11])


def genPatches(ax, x_pos, y_pos, x_size, y_size, color):
    p = patches.Rectangle((x_pos, y_pos), x_size, y_size, facecolor=color, edgecolor="black", linewidth=2)
    ax.add_patch(p)


# input: dp.DataFrame & node list (f.ex [0, 9 11])
def plotSignal(data, nodes, subplot):
    data = data.ix[:,nodes]
    data.plot(subplots=subplot)
    plt.xlabel("Time [s]")
    plt.ylabel("Voltage [pV]")
    plt.show()


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
            print("Node ID:",i,"Value:",data[i], "[pV]")
    return spikes, values


def main():
    N_ROWS = 1000
    fileName = "Data/2017-10-20_MEA2_100000rows_10sec.csv"
    data = readCSV(fileName, N_ROWS)

    subplot = True

    # Done
    #plotSignal(data, [1, 25, 56], subplot)
    #plotSpikes(data, N_ROWS)
    #frequenzyPlot(data, N_ROWS)


    # In development
    intesityPlot(data, N_ROWS)


if __name__ == "__main__":
    main()


    #TODO Generalize plotSpikes
    #TODO Plot cumulative values (using generalization of plotSpikes)