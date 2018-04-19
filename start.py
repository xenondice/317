import json
import time
import sys
import system.settings as settings
import system.environment as environment
from neural_presenters.virtual.virtual_led_model import VirtualLedModel
from neural_presenters.serial.serial_communication import SerialInterface
from neural_sources.file.file_server import FileServer
#from neural_sources.server.client import program_websocket
from neural_interpeters.random_mode import RandomMode
from neural_presenters.two_d_plot.two_d_plot import TwoDPlot

_presenter = None
_source = None
_interpeter = None
_led_colors = None

def main():
    global _led_colors, _presenter, _source, _interpeter
    _led_colors = bytearray([0] * (3 * settings.LEDS_TOTAL))

    if settings.NEURAL_PRESENTER == "virtual":
        _presenter = VirtualLedModel(_led_colors, settings.LED_MODEL)
    elif settings.NEURAL_PRESENTER == "serial":
        _presenter = SerialInterface()
    elif settings.NEURAL_PRESENTER == "2d-plot":
        _presenter = TwoDPlot()
    else:
        raise RuntimeError("Invalid presenter!")

    def loop(data):
        global _interpeter, _presenter, _led_colors
        _interpeter.render(data, _led_colors)
        _presenter.refresh(_led_colors)

    def error(message):
        print(message)

    if settings.NEURAL_SOURCE == "file":
        _source = FileServer(loop, error, _presenter)
    elif settings.NEURAL_SOURCE == "server":
        raise NotImplementedError()
    elif settings.NEURAL_SOURCE == "none":
        _source = None
    else:
        raise RuntimeError("Invalid source!")
    
    if settings.NEURAL_INTERPETER == "random":
        _interpeter = RandomMode()
    else:
        raise RuntimeError("Invalid interpeter!")


    if _source is None:
        frame_time = 1.0/settings.LED_REFRESHES_PER_SECOND
        neuron_data = [0] * settings.NEURAL_ELECTRODES_TOTAL
        while _presenter.running():
            past_time = time.time()
            
            for i in range(len(neuron_data)):
                neuron_data[i] = 0
            loop(neuron_data)

            delta = time.time() - past_time
            sleep_time = frame_time - delta
            if sleep_time < 0:
                print("Can't keep up!")
                sleep_time = 0
            
            time.sleep(sleep_time)
    else:
        _source.loop()

if __name__ == "__main__":
    try:
        environment.setup(sys.argv[1:])
    except SyntaxError as e:
        print("{}\nUse argument --help for more help.".format(e))
        exit(-1)
    main()