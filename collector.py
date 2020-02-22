import time
import zmq
import pprint
import sys
from utility import log

def result_collector(recive_socket,collector_id,send_socket):
    zmq_send = []
    zmq_recieve = []
    context = zmq.Context()
    for i in range(2):
        results_receiver = context.socket(zmq.PULL)
        results_receiver.bind("tcp://127.0.0.1:" + str( int(recive_socket) + i + int(collector_id) * 2 ))
    	zmq_recieve.append(results_receiver)
        result_sender = context.socket(zmq.PUSH)
    	result_sender.bind("tcp://127.0.0.1:" + str( int(send_socket) + i + int(collector_id) * 2 ) )  
        zmq_send.append(result_sender)

    while True:
        for i in range(2):
            result = zmq_recieve[i].recv_pyobj()
            log("recived frame number :" + str(result["frame_no"]) + " ", collector_id)
            zmq_send[i].send_pyobj(result)
        
result_collector(sys.argv[1],sys.argv[2],sys.argv[3])
