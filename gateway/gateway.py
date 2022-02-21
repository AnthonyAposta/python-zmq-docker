## receive data from crawlers and publish all the events 

from cmath import pi
import zmq

# Creates a socket instance
context = zmq.Context()


xsubSocket = context.socket(zmq.XSUB)
subPort = "tcp://0.0.0.0:5001"
xsubSocket.bind(subPort)

xpubSocket = context.socket(zmq.XPUB)
pubPort = "tcp://0.0.0.0:3231"
xpubSocket.bind(pubPort)

zmq.proxy(xpubSocket, xsubSocket)




