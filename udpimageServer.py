#!/usr/bin/env python3
'''UDP File Server'''
import socket
MAX_BYTES = 65507
host = ''
servPort = 5432

#STEP 1 - Create socket for data from a client
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#STEP 2 - Bind socket to socket address 
serverAddr = (host, servPort)		#2-tuple for server address info
sock.bind(serverAddr)

#STEP 3 - Repeatedly communicate with UDP clients
while True:	#loop forever
	print("Waiting for request from a client on port", servPort)
	print(sock.getsockname())
	filename, address = sock.recvfrom(MAX_BYTES)	#Receive filename from client 
	
	# Fetch data from file
	fin = open(filename, "rb")
	fileData = fin.read()
	fin.close()
	
	#Send file data to client
	sent = sock.sendto(fileData, address)
