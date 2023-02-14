import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print(f"Current libzmq version is {zmq.zmq_version()}")
print(f"Current  pyzmq version is {zmq.__version__}")
#  Do 10 requests, waiting each time for a response
for request in range(1):
    print(f"Sending request {request} ...")
    socket.send_string("GOOG")

    #  Get the reply.
    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")
