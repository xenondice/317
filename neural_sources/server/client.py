from system.settings import settings
import sys
import websocket
import threading
import json

class Client:
    def __init__(self, loopfunction, errorfunction):
        self.loopfunction = loopfunction
        self.errorfunction = errorfunction
        self.frequencies = [] * settings.NEURAL_ELECTRODES_TOTAL
        websocket.enableTrace(True)
        interval = int(1/settings.LED_REFRESHES_PER_SECOND * 1000 + 0.5)
        request = "ws://" + settings.SERVER_IP + ":" + settings.SERVER_PORT + "/data/" + str(interval)
        self.ws = websocket.WebSocketApp(request,
                                         on_message=self._on_message,
                                         on_error=self._on_error,
                                         on_close=self._on_close,
                                         on_open =self._on_open)
        self.timer = threading.Timer(settings.SERVER_TIMEOUT + 1/settings.LED_REFRESHES_PER_SECOND,
                                     self.timer_out())

    def loop(self):
        self.ws.run_forever()
        print("test")

    def _timer_out(self):
        self.errorfunction("Connection timeout")

    def _on_close(self):
        print("Connection closed")

    def _on_error(self, error):
        self.errorfunction("Connection error: {}".format(error))

    def _on_open(self):
        print("Connection established")

    def _on_message(self, message):
        self.timer.cancel()
        self.frequencies = json.loads(message)
        self.loopfunction(self.frequencies)
        self.timer = threading.Timer(settings.SERVER_TIMEOUT + 1 / settings.LED_REFRESHES_PER_SECOND,
                                     self.timer_out())
