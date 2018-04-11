import data_to_color as d2c


# TODO: Started but not finished

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
