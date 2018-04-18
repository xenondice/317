import system.settings as settings
import json

def setup(args):
    i = 0
    
    while i < len(args):
        arg = args[i]
        i += 1

        if arg == "--help":
            print("""
Script for visualizing neural data.
Defaults to showing a virtual model of random data.

General:
[--help]
    Print this help text and exit.
[--refresh-rate] <times per second>
    How often the LED model should refresh its image.
    The data between each refresh is added together.
[--datatype] [voltage | frequency]
    The type of data gathered from the neurons and passed to the interpeter.
[--led-model] <name>
    Name of the model file to use.
    It has to exist as a .json file in led_models.
[--interpeter] <name>
    Name of the script that reads neural data from the input source,
    and returns the LED colors for the model.
    The interpters lie in neural_interpeters.

Source (last argument will override the rest):
[--file] <location>
    Emulate neural server input with data from file.
    Will loop when the end of the file is reached.
[--server] <address>
    Recieve livestreamed neural data from the specified server.
    Default port is 6780, but can be changed with --port.
[--port] <port>
    Override default server port 6780.
[--no-input]
    Pass no neural data into the interpeter.

Presenter (last argument will override the rest):
[--virtual]
    Virtual 3D simulation of the model.
[--serial]
    Use an Arduino over USB to control a physical model.
[--2d-plot]
    2D grid plot / heatmap.
            """)
            exit(0)
        elif arg == "--refresh-rate":
            subarg = _get_float_subarg(i, args, "refresh rate")
            i += 1
            settings.LED_REFRESHES_PER_SECOND = subarg
        elif arg == "--datatype":
            subarg = _get_subarg(i, args, "datatype")
            i += 1
            if subarg != "voltage" and subarg != "frequency":
                raise SyntaxError("Invalid datatype!")
            settings.NERUAL_DATA_TYPE = subarg
        elif arg == "--led-model":
            subarg = _get_subarg(i, args, "led model").lower()
            i += 1
            settings.LED_MODEL_NAME = subarg
        elif arg == "--interpeter":
            subarg = _get_subarg(i, args, "interpeter").lower()
            i += 1
            settings.NEURAL_INTERPETER = subarg
        elif arg == "--file":
            subarg = _get_subarg(i, args, "file")
            i += 1
            settings.NEURAL_DATA_FILE = subarg
            settings.NEURAL_SOURCE = "file"
        elif arg == "--server":
            subarg = _get_subarg(i, args, "server")
            i += 1
            settings.SERVER_IP = subarg
            settings.NEURAL_SOURCE = "server"
        elif arg == "--port":
            subarg = _get_int_subarg(i, args, "port")
            i += 1
            settings.SERVER_PORT = subarg
        elif arg == "--no-input":
            settings.NEURAL_SOURCE = "none"
        elif arg == "--virtual":
            settings.NEURAL_PRESENTER = "virtual"
        elif arg == "--serial":
            settings.NEURAL_PRESENTER = "serial"
        elif arg == "--2d-plot":
            settings.NEURAL_PRESENTER = "2d-plot"
    
    # Setup derived variables
    try:
        settings.LED_MODEL = _load_led_model(settings.LED_MODEL_NAME)
    except IOError:
        raise SyntaxError("Could not load model file!")
    
    settings.LEDS_TOTAL = settings.LED_MODEL['led-quantity']

def _get_subarg(i, args, name):
    error = "No subargument for {}!".format(name)
    if i >= len(args):
        raise SyntaxError(error)
    subarg = args[i]
    if subarg.startswith('-'):
        raise SyntaxError(error)
    return subarg

def _get_int_subarg(i, args, name):
    subarg = _get_subarg(i, args, name)
    try:
        subarg = int(subarg)
    except ValueError:
        SyntaxError("{} subargument not a number!"
        .format(name.capitalize()))
    return subarg

def _get_float_subarg(i, args, name):
    subarg = _get_subarg(i, args, name)
    try:
        subarg = float(subarg)
    except ValueError:
        SyntaxError("{} subargument not a number!"
        .format(name.capitalize()))
    return subarg

def _load_led_model(model_name):
    model_file = open('models/{}.json'.format(model_name))
    model = json.loads(model_file.read())
    model_file.close()
    model['name'] = model_name
    model['led-quantity'] = len(model['led-strip'])
    return model