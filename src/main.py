import os
import base64
import pyrebase
from omx_trigger import play_video

databaseURL = os.environ["DBURL"]
fbCredentials = os.environ["DBCRED"]

with open("firebase-adminsdk.json", "wb") as fh:
    fh.write(base64.b64decode(fbCredentials))

config = {
    "apiKey": "apiKey",
    "authDomain": "lens-kiosk.firebaseapp.com",
    "databaseURL": databaseURL,
    "storageBucket": "lens-kiosk.appspot.com",
    "serviceAccount": "firebase-adminsdk.json",
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


def stream_handler(message):
    print("Playing video for " + message["data"])
    play_video(message["data"])


plu_stream = db.child("stores").child("Southampton").stream(stream_handler)

# def store_lookup(store):
#     result = db.child("stores").child(store).get()
#     print(result.val())
#

# store_lookup("Poole")
