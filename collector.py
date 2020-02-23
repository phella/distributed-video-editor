import time
import zmq
import pprint
import sys
from utility import log

def result_collector(recive_socket,collector_id,send_socket):
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:" + str( int(recive_socket) +  int(collector_id)  ))
    result_sender = context.socket(zmq.PUSH)
    result_sender.bind("tcp://192.168.43.144:" + str( int(send_socket) + int(collector_id) ))  

    while True:
        result = results_receiver.recv_pyobj()
        log("recived frame number :" + str(result["frame_no"]) + " ", collector_id)
        result_sender.send_pyobj(result)
        
result_collector(sys.argv[1],sys.argv[2],sys.argv[3])
