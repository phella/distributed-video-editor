import time
import zmq
import pprint
import sys
def result_collector(base_socket,collector_id):
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:"+base_socket)
    collecter_data = {}
    while True:
        result = results_receiver.recv_pyobj()
        print("collector"+str(collector_id)+"received")

result_collector(sys.argv[1],sys.argv[2])
