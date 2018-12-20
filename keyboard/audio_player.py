import AppKit
import time
from pydub import AudioSegment
from pydub.playback import play
import threading

class AudioPlayer:
    def __init__(self, filename):
        self.filepath="../data/bubble/"+str(filename)+".wav"
        # self.filepath="../data/bubble/1.wav"
        self.sound = AudioSegment.from_file(self.filepath, "wav")
    def play(self):
        play(self.sound)

if __name__ == "__main__":
    audioPlayer = AudioPlayer(1)
    thread = threading.Thread(target=audioPlayer.play)
    thread.start()
    