# coding: utf-8

import websocket
from websocket import create_connection
from threading import Thread
import time
import sys
import json
from mykeyboard.audio_player import AudioPlayer
import threading
import json
import ast
import threading


class WebsocketHandler:
    def __init__(self):
        self.host = "ws://localhost:8888/chatsocket"
        self.ws = create_connection(self.host)

    def send(self, message):
        message = json.dumps({"body": message})
        self.ws.send(message)

class WebsocketHandlerReceiver:
    def __init__(self):
        self.host = "ws://localhost:8888/chatsocket"

    def on_message(self, ws, message):
        message_dict = json.loads(message)
        body = message_dict['body']
        body = ast.literal_eval(body)
        print(f"message name is {body['name']}")
        thread = threading.Thread(target=AudioPlayer(body['category'], body['name']).play)
        thread.start()

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def on_open(self, ws):
        def run(*args):
            pass

        Thread(target=run).start()

    def start_receive(self):
        websocket.enableTrace(True)
        if len(sys.argv) < 2:
            host = self.host
        else:
            host = sys.argv[1]
        ws = websocket.WebSocketApp(host,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        ws.on_open = self.on_open
        ws.run_forever()

if __name__ == "__main__":
    ws = WebsocketHandler()
    ws.send("Hello, WebsocketHandler")

    wsr = WebsocketHandlerReceiver()
    wsr.start_receive()