#!/usr/bin/env python3 
'''UDP File Client'''
import socket
MAX_BYTES = 65507
host = "10.156.18.63"
servPort = 5432

#Create socket for data to/from server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#2-tuple for server address info
serverAddr = (host, servPort)

try:
	#Send data
	filename = "image1.jpg"
	sock.sendto(filename.encode(), serverAddr)
	#Receive response
	print("Waiting to receive")
	fileData, server = sock.recvfrom(MAX_BYTES)
	print("Received {} bytes".format(len(fileData)))
	
	#Write file data to a new file
	fout = open("image1copy.jpg","wb")
	fout.write(fileData)
	fout.close()
	
finally:
	print("Closing socket")
	sock.close()
