import zmq
import time

# Citation: ZeroMQ beginner tutorial

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


def get_company_name(ticker_symbol):
    
    ticker_to_company = {"AAPL": "Apple Inc.", "GOOG": "Alphabet Inc.", "MSFT": "Microsoft Corporation"}
    return ticker_to_company.get(ticker_symbol, "Unknown")


while True:
    
    ticker_symbol = socket.recv().decode()

    time.sleep(1)

    company_name = get_company_name(ticker_symbol)

    socket.send(company_name.encode())
