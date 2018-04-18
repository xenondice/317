import json
import sys

def load_led_model(model_name):
    model_file = open('models/{}.json'.format(model_name))
    model = json.loads(model_file.read())
    model_file.close()
    model['name'] = model_name
    model['led-quantity'] = len(model['led-strip'])
    return model

def setup_args(args):
    while len(args) != 0:
        arg = args.pop(0)

        if arg == "-h" or arg == "--help":
            print("""
Script for visualizing neural data.
Defaults to showing a virtual model of random data.

General:
[--help]
    Print this help text and exit.
[--refresh-rate] <times per second>
    How often the LED model should refresh its image.
    The data between each refresh is added together.
[--datatype] [voltage | spikes]
    The type of data gathered from the neurons and passed to the interpeter.
[--model] <name>
    Name of the model file to use.
    It has to exist as a .json file in neural_presenters/led_models.
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

def main():
    pass

if __name__ == "__main__":
    try:
        setup_args(sys.argv[1:])
    except SyntaxError as e:
        print("{}\nUse argument --help for more help.".format(e))
        exit(-1)
    main()