import sys
import os
from os import path


def play_video(PLU="default"):

    filepath = "/home/pi/videos/" + PLU + ".mp4"

    if path.exists(filepath):
        print("file found, playing...")
        os.system("omxplayer --display=5" + filepath)
    else:
        print("file not found, playing default video")
        os.system("omxplayer --display=5 /home/pi/videos/default.mp4")
