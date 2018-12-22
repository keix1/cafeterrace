# coding: utf-8

import keyboard
import time
import wave
from audio_player import AudioPlayer
import threading
import random

class KeyScanner:

    def __init__(self):
        self.audio_list = [AudioPlayer(self.map_keysound(str(i))) for i in range(1,9)]

    def key_press(self, key):
        print(key.name)
        thread = threading.Thread(target=self.audio_list[int(self.map_keysound(key.name))].play)
        thread.start()

    def map_keysound(self, input_string):
        char_list = [chr(i) for i in range(32, 127)]
        sound_list = [int(i/11) for i in range(0, 95)]
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

if __name__ == "__main__":
    key_scanner = KeyScanner()
    key_scanner.start_scan()
    while True:
        time.sleep(1)