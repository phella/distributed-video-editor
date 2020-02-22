import time
import zmq
import pprint
import sys
from utility import log

def result_collector(base_socket,collector_id,send_socket):
    zmq_sockets = []
    counter = 0
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:" + str(int(base_socket)))
    for i in range(int(2)):
    	zmq_socket = context.socket(zmq.PUSH)
    	zmq_socket.bind("tcp://127.0.0.1:" + str( int(send_socket) + counter) )  # need to check base_Socket type
        zmq_sockets.append(zmq_socket)
        counter += 1

    collecter_data = {}
    counter2 = 0
    while True:
        result = results_receiver.recv_pyobj()
        log("recived frame number :" + str(result["frame_no"]) + " ", collector_id)
        zmq_sockets[counter2].send_pyobj(result)
        counter2 = (counter2+1)% 2
result_collector(sys.argv[1],sys.argv[2],sys.argv[3])
