import keyboard
import time
import wave
from audio_player import AudioPlayer
import threading

def key_press(key):
    print(key.name)
    audioPlayer = AudioPlayer(map_keysound(key.name))
    thread = threading.Thread(target=audioPlayer.play)
    thread.start()

def map_keysound(input_string):
    char_list = [chr(i) for i in range(32, 127)]
    sound_list = [int(i/11) for i in range(1, 95)]
    
    try:
        return sound_list[char_list.index(input_string)]
    except ValueError:
        print("ValueError")
        return "1"

keyboard.on_press(key_press)

while True:
    time.sleep(1)