# coding: utf-8

import AppKit
import time
from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import ratio_to_db
import threading

class AudioPlayer:
    def __init__(self, filename):
        # self.filepath="../data/bubble/"+str(filename)+".wav"
        self.filepath="../data/cat/"+str(filename)+".mp3"
        # self.filepath="../data/bubble/1.wav"
        # self.filepath="../data/cat/cat.mp3"
        self.sound = AudioSegment.from_file(self.filepath, "mp3")
        self.sound = self.sound + ratio_to_db(0.3)
    def play(self):
        play(self.sound)

if __name__ == "__main__":
    audioPlayer = AudioPlayer(1)
    thread = threading.Thread(target=audioPlayer.play)
    thread.start()
    