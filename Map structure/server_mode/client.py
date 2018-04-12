def program_websocket(led_colors):
    websocket.enableTrace(True)
    def on_close(ws):
        print("Connection closed")
        exit()
    def on_error(ws, error):
        print("Connection error: {}".format(error))
        exit()
    def on_open(ws):
        print("Connection established")
    def on_message(ws, message):
        leds = json.loads(message)
        print(leds)
        for i in range(len(leds)):
            val = leds[i]
            if val > 255:
                val = 255
            led_colors[i*3] = val
            led_colors[i*3+1] = val
            led_colors[i*3+2] = val
        update(led_colors)
    ws = websocket.WebSocketApp("ws://10.22.65.72:6780/data/2000/"
    on_message = on_message,
    on_error = on_error,
    on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
