import json
import time
import sys
import system.settings as settings
import system.environment as environment
#from neural_presenters.virtual.virtual_led_model import *
#from neural_presenters.serial.serial_communication import *
#from neural_presenters.2d-plot.heatmap import *

_past_time = time.time()

def main():
    presenter = None
    if settings.NEURAL_PRESENTER == "virtual":
        raise NotImplementedError()
    elif settings.NEURAL_PRESENTER == "serial":
        raise NotImplementedError()
    elif settings.NEURAL_PRESENTER == "2d-plot":
        raise NotImplementedError()
    
    source = None
    if settings.NEURAL_SOURCE == "file":
        raise NotImplementedError() #read file
    if settings.NEURAL_SOURCE == "server":
        raise NotImplementedError()
    if settings.NEURAL_SOURCE == "none":
        raise NotImplementedError()
    
    interpeter = None
    if settings.NEURAL_INTERPETER == "random":
        raise NotImplementedError()

    def loop(data):
        global _past_time

        led_colors = interpeter.render(data)

        now_time = time.time()
        delta_time = now_time - _past_time
        _past_time = now_time
        time.sleep(1.0/settings.LED_REFRESHES_PER_SECOND - delta_time)
        
        presenter.refresh(led_colors)

    source.loop_function = loop
    source.start()

if __name__ == "__main__":
    try:
        environment.setup(sys.argv[1:])
    except SyntaxError as e:
        print("{}\nUse argument --help for more help.".format(e))
        exit(-1)
    main()