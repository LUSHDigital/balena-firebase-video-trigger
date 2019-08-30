import os
import base64
import pyrebase
from omx_trigger import play_video

databaseURL = os.environ["DBURL"]
fbCredentials = os.environ["DBCRED"]
dbParent = os.environ["DBPARENT"]
dbChild = os.environ["DBCHILD"]

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
    plu = str(message["data"])
    print("Playing video for " + plu)
    play_video(plu)


plu_stream = db.child(dbParent).child(dbChild).stream(stream_handler)

# def store_lookup(child):
#     result = db.child(dbParent).child(child).get()
#     print(result.val())
#

# store_lookup(dbChild)
