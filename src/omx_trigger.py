import sys
import os


def play_video(PLU="default"):
    os.system("omxplayer --display=5 /home/pi/videos/" + PLU + ".mp4")
