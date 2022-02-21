# crawler to receive data from twitter api
from email import message
import imp
import json
from os import stat
import zmq
from time import sleep
import tweepy
from dotenv import load_dotenv
import os


class Intantiate(tweepy.Stream):

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret)

        context = zmq.Context()
        self.socket = context.socket(zmq.PUB)

        print("conneting to xpub")
        # Creates a socket instance

        #socket.connect("tcp://0.0.0.0:5001")
        self.socket.connect("tcp://gateway-service:5001")
        self.topic = 'crawler.python'


    def message_encoder(self, topic_str: str, message_dict: dict) -> bytes:

        message_json = json.dumps(message_dict)
        
        message = topic_str + ' ' + message_json

        encoded_message = str.encode(message)

        return encoded_message 

    def on_status(self, status):
        
        status_json = status._json

        message = {"text": status_json["text"], "timestamp_ms": status_json["timestamp_ms"]}
        self.socket.send(self.message_encoder(self.topic, message))

        print(message)


if __name__ == "__main__":

    load_dotenv()
    consumer_key = os.getenv('consumer_key')
    consumer_secret = os.getenv('consumer_secret')
    access_token = os.getenv('access_token')
    access_token_secret = os.getenv('access_token_secret')


    instance = Intantiate(consumer_key, consumer_secret, access_token, access_token_secret)
    instance.filter(track=["python"])


