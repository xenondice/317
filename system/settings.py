
# Serial
SERIAL_BAUD_RATE = 115200

# 2D plot
PLOT_COLOR_FROM = 'green'
PLOT_COLOR_TO = 'red'

# Server
SERVER_IP = '10.22.67.23'
SERVER_PORT = '6780'
SERVER_TIMEOUT = 5

# Data flow
NEURAL_ELECTRODES_TOTAL = 60
NEURAL_PRESENTER = 'virtual'
NEURAL_SOURCE = 'server'
NEURAL_INTERPETER = 'random'
NERUAL_DATA_TYPE = 'frequency'

# Visualization
LED_REFRESHES_PER_SECOND = 60
LED_MODEL_NAME = 'large_cube'


### Derived variables (initialized in environment.py) ###

LEDS_TOTAL = None
LED_MODEL = None

NEURAL_DATA_FILE = None
