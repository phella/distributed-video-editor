import time
import zmq
import random
import cv2
import numpy as np
import sys
# send socket
def consumer(base_socket,consumer_id):
    print ("I am consumer " + str(consumer_id))
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:" + str(int(base_socket)))
    # send work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:5058")

    while True:
        result = consumer_receiver.recv_pyobj()
        print(str(consumer_id)+ "has recieved")
        ret2,result["img"] = cv2.threshold(result["img"],0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        consumer_sender.send_pyobj(result)
consumer(sys.argv[1],sys.argv[2])
