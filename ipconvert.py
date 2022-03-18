#!/usr/bin/env python3

"""Program recieves IP from user and converts IPv4 address to 32 binary HEX value

Usage: chmod +x ipconvert.py

Usage Example: ipconvert.py 192.168.74.96

"""
import socket
import sys

def main(argv):
	if len(argv) != 2:
		print("USAGE: ipconvert <ip address>")
		
	else:
		inputtedIP = argv[1]
		
		convertIP(inputtedIP)
	
def convertIP(inputtedIP):
	"""Function recieves IP address from command line and converts to 32bit HEX value """
	hexList = []
	packedIP = socket.inet_aton(inputtedIP)
	for b in packedIP:
		hexList.append(hex(b))
	print("{}".format(hexList))



if __name__ == "__main__":
	main(sys.argv)
	
