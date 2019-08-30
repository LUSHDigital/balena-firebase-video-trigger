import sys
import os
from os import path


def play_video(PLU="default"):

    filepath = "/home/pi/videos/" + PLU + ".mp4"
    print("filepath is: " + filepath)

    if not path.exists(filepath):
        print("can not find file, playing default")
        filepath = "/home/pi/videos/default.mp4"

    print("filepath is now: " + filepath)
    print("playing...")
    os.system("omxplayer --display=5 " + filepath)
