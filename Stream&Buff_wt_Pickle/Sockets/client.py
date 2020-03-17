import socket
import pickle

HEADERSIZE = 10

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))

while True:
	complete_message=b''
	new_message=True
	
	while True:
	
		message = s.recv(12)
	
		if new_message:
			print(f"new message length: {message[:HEADERSIZE]}")
			messagelen = int(message[:HEADERSIZE])
			new_message = False

		complete_message += message
		
		if len(complete_message)-HEADERSIZE == messagelen:
			print("Complete message received")
			print(complete_message[HEADERSIZE:])
			d = pickle.loads(complete_message[HEADERSIZE:])
			print(d)

			new_message = True
			complete_message = b''

	print(complete_message)

