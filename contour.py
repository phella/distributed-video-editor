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
    contour_receiver.connect("tcp://192.168.43.144:" + str(int( base_socket) + int(contour_id)))
    # send work
    contour_sender = context.socket(zmq.PUSH)
    contour_sender.connect("tcp://127.0.0.1:" + send_socket)

    while True:
        result = contour_receiver.recv_pyobj()
        contours = skimage.measure.find_contours(result["img"] , 100) #second param unkown
        contour_sender.send_pyobj( {"frame_no" : result["frame_no"] , "res" : contours} )
        log("frame no" + str(result["frame_no" ] ) + " processed successfully" , contour_id )
consumer(sys.argv[1],sys.argv[2],sys.argv[3])
