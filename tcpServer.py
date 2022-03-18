import socket

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind(('',5050))
serverSock.listen()

while True:
	print("Waiting for connection")
	connectSock, clientAddr = serverSock.accept()
	print("Connection from", clientAddr)
	
	while True:
		dataInBytes = connectSock.recv(1024)
		
		if not dataInBytes:
			break
		connectSock.sendall(dataInBytes)
		
	connectSock.close()
