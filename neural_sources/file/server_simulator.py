import pandas as pd
import spike_detection


class csv:
    def __init__(self, file_name, skip_rows, n_rows):
        self.file_name = file_name
        self.skip_rows = skip_rows
        self.n_rows = n_rows

    def get_file_name(self):
        return self.file_name

    def get_skip_rows(self):
        return self.skip_rows

    def get_n_rows(self):
        return self.n_rows

    def set_skip_rows(self, skip_rows):
        self.skip_rows = skip_rows


def read_CSV(fileName, N_ROWS, skip_rows):
    return pd.read_csv(fileName, skiprows=skip_rows, nrows=N_ROWS, index_col=0)


def simulate_server(data, file_name):
    file_name = "data/" + file_name

    read_CSV(file_name)