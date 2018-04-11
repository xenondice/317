import random as rand


def plot_spikes(data):
    return 0


def color_grouping(index, values, value_per_group):
    if values[index] <= value_per_group:
        return 0
    elif value_per_group < values[index] <= 2 * value_per_group:
        return 1
    elif 2 * value_per_group < values[index] <= 3 * value_per_group:
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


if __name__ == '__main__':
    data = [0] * 60
    for i in range(len(data)):
        data[i] = rand.randint(0, 9)
    print(data)

    plot_spikes(data)
