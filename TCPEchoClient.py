#!/usr/bin/env python3
"""TCP client program recieves message from user sends and recieves to and from TCP server"""
import socket
import sys
def main(argv):
	
	try:
	
		message = argv[1]
		serverIP = "127.0.0.1"
		serverPort = 6060
		clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sockAddr = ("127.0.0.1", 6060)
		clientSock.connect(sockAddr)
		msgBytes = message.encode("UTF-8")
		clientSock.sendall(msgBytes)
		print("Waiting for server to send back")
	
		data = clientSock.recv(1024)
		decodedData = data.decode()
		print(decodedData.upper())
		clientSock.close()
		
	except IndexError:
		print("IndexError\nUsage: ./TCPEchoClient.py <message here>")
	
if __name__ == "__main__":
	main(sys.argv)
