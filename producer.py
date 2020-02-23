import time
import zmq
import cv2
import numpy as np
import sys

def producer( base_socket):
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:" + base_socket) 

    vidcap = cv2.VideoCapture('test.mp4')
    success,image = vidcap.read()
    frame_no = 0
    # Start your result manager and workers before you start your producers
    while( success ):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        zmq_socket.send_pyobj({"frame_no": frame_no,"img" : img})
        frame_no += 1
        success,image = vidcap.read()

producer(sys.argv[1] )
