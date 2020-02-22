import time
import zmq
import sys
from utility import log

def result_collector(base_socket):
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:" + base_socket)


    collecter_data = {}
    while True:
        result = results_receiver.recv_pyobj()

result_collector(sys.argv[1])
