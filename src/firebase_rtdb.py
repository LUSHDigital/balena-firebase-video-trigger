import os
import base64
import pyrebase

databaseURL = os.environ['DBURL']
fbCredentials = os.environ['DBCRED']

with open("firebase-adminsdk.json", "wb") as fh:
    fh.write(base64.b64decode(fbCredentials))

config = {
  "apiKey": "apiKey",
  "authDomain": "lens-kiosk.firebaseapp.com",
  "databaseURL": databaseURL,
  "storageBucket": "lens-kiosk.appspot.com",
  "serviceAccount": "firebase-adminsdk.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def store_lookup(store):
    result = db.child("stores").child(store).get()
    print(result.val())

store_lookup("Poole")

def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

my_stream = db.child("stores").stream(stream_handler)
