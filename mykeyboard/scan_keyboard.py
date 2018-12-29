# coding: utf-8

import sys
import os
cwd = os.getcwd()
sys.path.append(cwd + '/mykeyboard/')
sys.path.append(cwd + '/client/')
import keyboard
import time
import wave
from audio_player import AudioPlayer
import threading
import random
import json
from ws_client import WebsocketHandler
from ws_client import WebsocketHandlerReceiver

class KeyScanner:

    def __init__(self, connection=None, server_connection=None):
        self.audio_list = [AudioPlayer("bubble", str(self.map_keysound(str(i)))) for i in range(0,9)]
        self.connection = connection
        self.server_connection = server_connection

    def key_press(self, key):
        print(key.name)
        thread = threading.Thread(target=self.audio_list[int(self.map_keysound(key.name))].play)
        thread.start()

        message = {"category":"bubble", "name":str(self.map_keysound(key.name))}
        try:
            self.connection.send(message)
        except Exception as e:
            print(e)

    def map_keysound(self, input_string):
        # char_list = [chr(i) for i in range(32, 127)]
        # sound_list = [int(i/11) for i in range(0, 95)]
        rand = random.randint(1,8)
        print(str(rand))
        try:
            # return sound_list[char_list.index(input_string)]
            return rand
        except ValueError:
            print("ValueError")
            return "1"

    def start_scan(self):
        keyboard.on_press(self.key_press)
        self.server_connection.start_receive()

if __name__ == "__main__":
    key_scanner = KeyScanner()
    key_scanner.start_scan()
    while True:
        time.sleep(1)