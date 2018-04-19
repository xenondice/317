import pandas as pd
import system.settings as settings
import time

class FileServer:
    def __init__(self):
        self.file_path = settings.NEURAL_DATA_FILE
        self.skip_rows = 6


    def read_CSV(fileName, N_ROWS):
        return pd.read_csv(fileName, skiprows=skip_rows, nrows=N_ROWS, index_col=0)


    def loop(self, loop_function, _presenter):
        frame_time = 1.0 / settings.LED_REFRESHES_PER_SECOND
        while _presenter.running():
            past_time = time.time()
            loop_function()
            delta = time.time() - past_time
            sleep_time = frame_time - delta
            if sleep_time < 0:
                print("Can't keep up!")
                sleep_time = 0

            time.sleep(sleep_time)


if __name__ == '__main__':
    pass