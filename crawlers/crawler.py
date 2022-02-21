# crawler to receive data from twitter api

import json
from pydoc_data import topics
import zmq
from time import sleep


def message_encoder(topic_str: str, message_dict: dict) -> bytes:

    message_json = json.dumps(message_dict)
    
    message = topic_str + ' ' + message_json

    encoded_message = str.encode(message)

    return encoded_message 

# Creates a socket instance
context = zmq.Context()
socket = context.socket(zmq.PUB)

print("conneting to xpub")
socket.connect("tcp://gateway-service:5001")
#socket.connect("tcp://0.0.0.0:5001")

topic = 'crawler.crawler1'

# Sends a string message
message_id = 0
while True:

    message_id += 1
    message = {"message": "this is a message", "id": message_id}
    socket.send( message_encoder(topic, message) )
    print(message)
    sleep(1)
