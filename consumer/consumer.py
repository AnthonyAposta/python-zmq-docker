# consumer to read events from the pipline 

from email import message
import zmq

context = zmq.Context()
# Socket to receive messages
receiver = context.socket(zmq.SUB)
receiver.connect('tcp://gateway-service:3231')
receiver.subscribe("")

print('waiting for messages')
while True:

    message = receiver.recv_json()
    print(message)