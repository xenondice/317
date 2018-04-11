class Settings:
    def __init__(self, BAUDRATE, NUM_LEDS, COLOR_FROM, COLOR_TO, SIMULATION, ACTIVE_MODEL_NAME, PROGRAM):
        self.BAUDRATE = BAUDRATE
        self.NUM_LEDS = NUM_LEDS
        self.COLOR_FROM = COLOR_FROM
        self.COLOR_TO = COLOR_TO
        self.SIMULATION = SIMULATION
        self.ACTIVATE_MODEL_NAME = ACTIVE_MODEL_NAME
        self.PROGRAM = PROGRAM

    def get_color_from(self):
        return self.COLOR_FROM

    def get_color_to(self):
        return self.COLOR_TO

    def get_num_leds(self):
        return self.NUM_LEDS
