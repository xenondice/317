import pandas as pd
import system.settings as settings
import time

def read_CSV(fileName, N_ROWS, skip_rows=6):
    return pd.read_csv(fileName, skiprows=skip_rows, nrows=N_ROWS, index_col=0)


def live_stream_skipes():
    file_path = 'data/2017-10-20_MEA2_100000rows_10sec.csv'
    n_lines = 10000/settings.LED_REFRESHES_PER_SECOND
    skip = 6

    while skip < 100000:
        raw_data = read_CSV(file_path, n_lines, skip_rows=skip)
        skip += n_lines
        time.sleep(1/settings.LED_REFRESHES_PER_SECOND)


def live_stream_volt():
    file_path = 'data/2017-10-20_MEA2_100000rows_10sec.csv'


if __name__ == '__main__':
    t1 = time.time()
    time.sleep(1)
    t2 = time.time()
    print(t2-t1)