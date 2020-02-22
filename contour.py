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
    contour_receiver.connect("tcp://127.0.0.1:" + base_socket)
    # send work
    contour_sender = context.socket(zmq.PUSH)
    contour_sender.connect("tcp://127.0.0.1:"+send_socket)

    while True:
        result = contour_receiver.recv_pyobj()
        result=skimage.mesure.findContours(result["img"])
        contour_sender.send_pyobj(result)
consumer(sys.argv[1],sys.argv[2],sys.argv[3])
