"""Program to scan ports 1-1024 and return protocol type, port number and port service name

Usage: Run from command line

Usage Example: python3 portScan.py
 
"""
import socket
ports = []
for i in range(1,1024):
	ports.append(i)
	
proto1 = "tcp"
proto2 = "udp"

for port in ports:
	try:
		tcpServ = socket.getservbyport(port, proto1)
		print(proto1, " port: ", port, " - service name: ", tcpServ)
		
	except:
		print(proto1, " port: ", port, " - not found")
		
for port in ports:
	try:
		udpServ = socket.getservbyport(port, proto2)
		print(proto2, " port: ", port, " - service name: ", udpServ)
		
	except:
		print(proto2, " port: ", port, " - not found")
