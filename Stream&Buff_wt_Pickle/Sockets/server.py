import socket
import time
import pickle

d = {1:"This", 2:"is", 3:"completely", 4:"random"}

HEADERSIZE = 10

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established!")
	
	message = pickle.dumps(d)
	
	message=bytes(f'{len(message):<{HEADERSIZE}}',"utf-8")+message

	clientsocket.send(message)

	
		