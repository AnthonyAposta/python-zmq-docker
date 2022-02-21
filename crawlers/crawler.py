# crawler to receive data from twitter api

from email import message
import json
import zmq
from time import sleep
#import tweepy

# Creates a socket instance
context = zmq.Context()
socket = context.socket(zmq.PUB)

print("conneting to xpub")
socket.connect("tcp://gateway-service:5001")

# Sends a string message
message_id = 0
while True:

    message_id += 1
    message = {"message": "this is a message", "id": message_id}
    message_json = json.dumps(message)
    socket.send_json(message_json)
    print(message_json)
    sleep(1)
