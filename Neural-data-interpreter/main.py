import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def plotSpikes(data, N_ROWS):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    for i in range(N_ROWS):
        spikes = spikeDetection(data.iloc[i])
        x_pos = 0.6
        y_pos = 0.6
        x_size = 0.8
        y_size = 0.8

        j = 0
        for spike in spikes:
            if spike == True:
                p = patches.Rectangle((x_pos, y_pos), x_size, y_size, facecolor="green", edgecolor="black", linewidth=2)
                ax.add_patch(p)

            else:
                p = patches.Rectangle((x_pos, y_pos), x_size, y_size, facecolor="none", edgecolor="black", linewidth=2)
                ax.add_patch(p)
            if j == 9:
                y_pos += y_size + 0.2
                x_pos = 0.6
                j = 0
            else:
                x_pos += x_size + 0.2
                j += 1

        plt.ylim([0, 7])
        plt.xlim([0, 11])
        plt.title("Iteration: " + str(i) + "\nTime: " + str(i/10000) +"s")
        plt.draw()
        plt.pause(0.001)
        ax.clear()


# input: dp.DataFrame & node list (f.ex [0, 9 11])
def plotSignal(data, nodes, subplot):
    data = data.ix[:,nodes]
    data.plot(subplots=subplot)
    plt.xlabel("Time [s]")
    plt.ylabel("Voltage [pV]")
    plt.show()


# Returns pd.DataFrame with time [s] as index.
def readCSV(fileName, N_ROWS):
    raw_data = pd.read_csv(fileName, skiprows=6,nrows=N_ROWS)
    raw_data.iloc[:,0] = raw_data.iloc[:,0]*10**-6
    raw_data.set_index("TimeStamp [µs]", inplace=True)
    return raw_data


def spikeDetection(data):
    n_colums = data.shape[0]
    spikes = [False]*n_colums
    threshold = -2.5*10**7

    for i in range(n_colums):
        if data[i] <= threshold:
            spikes[i] = True
            print("Node ID:",i,"Value:",data[i], "[pV]")

    return spikes


def main():
    N_ROWS = 10000
    fileName = "Data/2017-10-20T16-07-47MEA2 _Recording-0_(Data Acquisition (1);MEA2100; Electrode Raw Data1).csv"
    data = readCSV(fileName, N_ROWS)

    subplot = True
    plotSignal(data, [1, 25, 56], subplot)
    plotSpikes(data, N_ROWS)



if __name__ == "__main__":
    main()


    #TODO Generalize plotSpikes
    #TODO Plot cumulative values (using generalization of plotSpikes)