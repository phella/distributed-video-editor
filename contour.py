import time
import zmq
import random
import cv2
import numpy as np
import sys
import math
from utility import log
import skimage


# send socket
def consumer(base_socket,contour_id,send_socket):
    context = zmq.Context()
    contour_receiver = context.socket(zmq.PULL)
    contour_receiver.connect("tcp://192.168.43.144:" + str(int( base_socket) + int(contour_id) // 2 ))
    # send work
    contour_sender = context.socket(zmq.PUSH)
    contour_sender.connect("tcp://127.0.0.1:" + send_socket)

    while True:
        result = contour_receiver.recv_pyobj()
        contours = skimage.measure.find_contours(result["img"] , 0.8) 
        boxes = []
        for box in contours:
                boundaries = {}
                boundaries["Xmin"] = int(np.min(box[:,1]))
                boundaries["Xmax"] = int(np.max(box[:,1]))
                boundaries["Ymin"] = int(np.min(box[:,0]))
                boundaries["Ymax"] = int(np.max(box[:,0]))
                boxes.append(boundaries)

        contour_sender.send_pyobj( {"frame_no" : result["frame_no"] , "res" : boxes} )
        log("frame no" + str(result["frame_no" ] ) + " processed successfully" , contour_id )
consumer(sys.argv[1],sys.argv[2],sys.argv[3])
