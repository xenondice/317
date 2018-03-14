import json

BAUDRATE = 115200
NUM_LEDS = 240
COLOR_FROM = 'green'
COLOR_TO = 'red'
SIMULATION = False
ACTIVE_MODEL_NAME = 'cube'

def _load_model(model_name):
    model_file = open('models/{}.json'.format(model_name))
    model = json.loads(model_file.read())
    model_file.close()
    model['name'] = model_name
    model['led-quantity'] = len(model['led-strip'])
    return model

MODEL = _load_model(ACTIVE_MODEL_NAME)