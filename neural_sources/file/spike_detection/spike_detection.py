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
