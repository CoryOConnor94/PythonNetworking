import socket
serverSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverPort = 12000
serverSock.bind(('',serverPort))
serverSock.listen(1)
print("Listening on port", serverPort)
while True:
	connectSock, addr = serverSock.accept()
	print("Connection with ", addr)
	sentence = connectSock.recv(1024).decode() # can receive upto 1024 bytes
	capitalizedSentence = sentence.upper()
	connectSock.send(capitalizedSentence.encode())
	connectSock.close()
