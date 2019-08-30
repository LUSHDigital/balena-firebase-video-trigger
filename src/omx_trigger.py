import sys
import threading
import os
from os import path

threads = []


def omx_play(file):
    os.system("omxplayer --display=5" + file)


def video_trigger(PLU="default"):

    filepath = "/home/pi/videos/" + PLU + ".mp4"

    if path.exists(filepath):
        print("file found, playing...")
        omx_play(filepath)
        # t = threading.Thread(target=omx_play, args=(filepath,))
        # threads.append(t)
        # t.start()
    else:
        print("file not found, playing default video")
        omx_play("/home/pi/videos/default.mp4")
        # t = threading.Thread(target=omx_play, args=("/home/pi/videos/default.mp4",))
        # threads.append(t)
        # t.start()
