#!/usr/bin/env python3
""" TCP server program that recieves echo message from client"""
import socket

def main():
	serverIP = "127.0.0.1"
	serverPort = 6060
	serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socketAddr = ("", 6060)
	serverSock.bind(socketAddr)
	serverSock.listen(1)
	
	while True:
		
		print("Waiting for client to connect")
		connectSock, addr = serverSock.accept()
		data = connectSock.recv(50000)
		connectSock.sendall(data)
		decodedData = data.decode()
		print(decodedData)
		connectSock.close()
	
			
	
		
if __name__ =="__main__":
	main()
