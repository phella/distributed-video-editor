import time
import zmq
import cv2
import numpy as np
import sys

def producer(num_processes , base_socket):
    context = zmq.Context()
    zmq_sockets = []
    counter = 0
    for i in range(int(num_processes)):
    	zmq_socket = context.socket(zmq.PUSH)
    	zmq_socket.bind("tcp://127.0.0.1:" + str( int(base_socket) + counter) )  # need to check base_Socket type
        print("eh yaba"+ str( int(base_socket) + counter))
        zmq_sockets.append(zmq_socket)
        counter += 1

    vidcap = cv2.VideoCapture('test.mp4')
    success,image = vidcap.read()
    frame_no = 0
    counter2 = 0
    # Start your result manager and workers before you start your producers
    while( success ):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        zmq_sockets[counter2].send_pyobj({"frame_no": frame_no,"img" : img})
        frame_no += 1
        counter2 = (counter2+1)% counter
        success,image = vidcap.read()

producer(sys.argv[1] , sys.argv[2])
