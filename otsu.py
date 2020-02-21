import time
import zmq
import random
import cv2
import numpy as np

# send socket 
def consumer():
    consumer_id = random.randrange(1,10005)
    print ("I am consumer " + str(consumer_id))
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    # send work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:5558")
    
    while True:
        result = consumer_receiver.recv_pyobj()
        ret2,result["img"] = cv2.threshold(result["img"],0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        consumer_sender.send_pyobj(result)
consumer()
