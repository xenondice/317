from colour import Color


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


def generate_color_gradient(settings):
    color1 = Color(settings.get_color_from())
    return list(color1.range_to(Color(settings.get_color_to()), 10))


def data_to_hex(data, settings):
    colors = generate_color_gradient(settings)
    hex_data = [0] * 60
    for i in range(len(data)):
        hex_data[i] = colors[int(data[i])].get_hex_l()
    return hex_data


def data_to_bytearray(data, settings):
    hex_array = data_to_hex(data, settings)
    num_leds_cluster = int(settings.get_num_leds() / 60)
    byte_arr = bytearray([0, 0, 0] * settings.get_num_leds())
    for i in range(len(hex_array)):
        for j in range(num_leds_cluster):
            index = i * 3 * num_leds_cluster + 3 * j
            byte_arr[index:index + 3] = bytearray.fromhex(hex_array[i][1:])
    return byte_arr
