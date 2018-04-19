import time

import pandas as pd

import system.settings as settings


class FileServer:
    def __init__(self, loop_function, error_function, presenter):
        self.file_path = settings.NEURAL_DATA_FILE
        self.skip_rows = 6
        self.loop_function = loop_function
        self.presenter = presenter

    def spike_detection(self, data):
        n_rows, n_colums = data.shape
        print('colums = ', n_columns)
        print('rows = ', n_rows)
        spikes = [[False] * n_columns] * n_rows
        volt = [[0] * n_columns] * n_rows
        threshold = -1 * 10 ** 7

        for i in range(n_rows):
            for i in range(n_columns):
                volt[i][j] = data[i][j]
                if data[i] <= threshold:
                    spikes[i][j] = True
                    # print("Node ID:",i,"Value:",data[i], "[pV]")
        return spikes, volt

    def read_CSV(self, N_ROWS):
        lines = pd.read_csv(self.file_path, skiprows=self.skip_rows, nrows=N_ROWS, index_col=0)
        self.skip_rows += N_ROWS
        return self.spike_detection(lines)

    def loop(self):
        frame_time = 1.0 / settings.LED_REFRESHES_PER_SECOND
        while self.presenter.running():
            past_time = time.time()
            if settings.NERUAL_DATA_TYPE == 'frequency':
                N_ROWS = int(10000 * frame_time)
                spike, _ = self.read_CSV(N_ROWS)
                processed_data = [0] * settings.NEURAL_ELECTRODES_TOTAL
                for i in range(len(spike)):
                    for j in range(len(spike[i])):
                        if spike[i][j]:
                            processed_data[j] += 1
            elif settings.NERUAL_DATA_TYPE == 'voltage':
                N_ROWS = 1
                _, processed_data = self.read_CSV(N_ROWS)
            self.loop_function(processed_data)
            delta = time.time() - past_time
            sleep_time = frame_time - delta
            if sleep_time < 0:
                print("Can't keep up!")
                sleep_time = 0

            time.sleep(sleep_time)


if __name__ == '__main__':
    pass
