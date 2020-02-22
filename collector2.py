import time
import zmq
import sys
from utility import log , listToString

def result_collector(base_socket):
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:" + base_socket)


    collecter_data = {}
    while True:
        result = results_receiver.recv_pyobj()
        log("frame no " + str(result["frame_no"]) + " countours = " + listToString( result["res"] ) )

result_collector(sys.argv[1])
