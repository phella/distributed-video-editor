import time
import zmq
import pprint
import sys
from utility import log

def result_collector(base_socket,collector_id):
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:" + base_socket)
    collecter_data = {}
    while True:
        result = results_receiver.recv_pyobj()
        log("recived frame number :" + str(result["frame_no"]) + " ", collector_id)

result_collector(sys.argv[1],sys.argv[2])
