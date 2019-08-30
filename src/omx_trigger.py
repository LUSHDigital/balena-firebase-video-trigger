import sys
import thread
import os
from os import path


def omx_play(file):
    os.system("omxplayer --display=5" + file)


def video_trigger(PLU="default"):

    filepath = "/home/pi/videos/" + PLU + ".mp4"

    if path.exists(filepath):
        print("file found, playing...")
        thread.start_new_thread(omx_play(filepath), ())
    else:
        print("file not found, playing default video")
        thread.start_new_thread(omx_play("/home/pi/videos/default.mp4"), ())
