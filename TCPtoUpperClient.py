import socket
serverName = "192.168.56.1" # replace with IP address of your server
serverPort = 12000
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect((serverName,serverPort))
sentence = "abcdefghijklmnopqrstuvwxyz"
clientSock.sendall(sentence.encode())
modifiedSentence = clientSock.recv(len(sentence))
clientSock.close()
print("From Server:", modifiedSentence.decode())
