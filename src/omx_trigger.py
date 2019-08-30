import sys
import os
from os import path


def play_video(PLU="default"):

    filepath = "/home/pi/videos/" + PLU + ".mp4"

    if not path.exists(filepath):
        filepath = "/home/pi/videos/default.mp4"

    print("playing...")
    os.system("omxplayer --display=5" + filepath)
