#!/usr/bin/env python3
import socket
import sys

def is_port_open(host, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((host,port))
		if result == 0:
			return True
		else:
			return False
		s.close()
	except keyboardInterrupt:
		print("\nKeyboard interrupt - end program")
		sys.exit()
	except socket.gaierror:
		print("\n Hostname Could not be resolved !!!")
		sys.exit()
	except OSError as err:
		print("Socket error - ", err)
		sys.exit()
		
if __name__=="__main__":
	print("TCP Port Scanner >> ")
	host = "localhost"
	open_ports = []
	for port in range(1,65535):
		if is_port_open(host, port) is True:
			open_ports.append(port)
			
	print("Open ports: ", open_ports)
