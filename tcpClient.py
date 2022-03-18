import socket
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSockAddr = ('', 5050)
clientSock.connect(serverSockAddr)

dataOutStr = "Data to be sent to server and back"
dataOutBytes = dataOutStr.encode()
clientSock.sendall(dataOutBytes)
numBytes = len(dataOutBytes)

dataInBytes = b''
while len(dataInBytes) < numBytes:
	dataInBytes += clientSock.recv(numBytes - len(dataInBytes))
	if not dataInBytes:
		break
		
dataInStr = dataInBytes.decode()
remoteAddr = clientSock.getpeername()
print("received", dataInStr, "back from server", remoteAddr)

clientSock.close()
