
# Serial
SERIAL_BAUD_RATE = 115200

# Plotter
PLOTTER_COLOR_FROM = 'green'
PLOTTER_COLOR_TO = 'red'

# Server
SERVER_IP = '127.0.0.1'
SERVER_PORT = 6780

# Data flow
NEURAL_PRESENTER = 'virtual'
NEURAL_SOURCE = 'none'
NEURAL_INTERPETER = 'random'
NERUAL_DATA_TYPE = 'frequency'

# Visualization
LED_REFRESHES_PER_SECOND = 5
LED_MODEL_NAME = 'large_cube'


### Derived variables (initialized in environment.py) ###

LEDS_TOTAL = None
LED_MODEL = None

NEURAL_DATA_FILE = None