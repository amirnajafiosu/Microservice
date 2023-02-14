# Microservice
Microservice Implementation Communication Contract

A. Clear instructions for how to REQUEST data from the microservice you implemented. Include an example call. 
    This example uses Python3: Must use ZeroMQ for socket.
    Step1) (add code) import zmq
    Step2) Socket to talk to server - (add code) socket = context.socket(zmq.REQ)
    Step3) This is a local connection - socket cont. (add code) socket = context.socket(zmq.REQ)
    Step4) Request data - (add code) socket.send(<your user input>)
    Example call) 
      1 | ticker_symbol = input("Enter a stock ticker symbol")
      2 | socket.send(ticker_symbol.encode())
      
B. Clear instructions for how to RECEIVE data from the microservice you implemented
    Step1) assign recieve code to your variable (add code) <your variable> = socket.recv()
    
C. UML sequence diagram showing how requesting and receiving data work. Make it detailed enough that your partner (and your grader) will understand!

[uml sequence diagram](https://user-images.githubusercontent.com/81668533/218878894-4e1458f5-588e-4bf8-97bf-748b460d7fc6.png)
