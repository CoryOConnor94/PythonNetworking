#!/usr/bin/env python3

"""Program uses socket module functions to extract MAC address of given interface 

Usage: chmod +x getMAC.py

Usage example: sudo getMAC.py enp0s3

"""
from socket import socket, AF_PACKET, SOCK_RAW
import sys

def main(argv):
	if len(argv) != 2:
		print("USAGE: getMAC <iface name>")
		
	else:
		userInt = argv[1]
		getMAC(userInt)
def getMAC(userInt):
		"""Function extracts MAC address and converts bytes to HEX and displays"""
		rawsock = socket(AF_PACKET, SOCK_RAW)
		port = 0
		rawsock.bind((userInt, port))
		sockname = rawsock.getsockname()
		intMac = sockname[4].hex(":")
		rawsock.close()
		print(f"The MAC address of {userInt} is {intMac}")
		
if __name__ == "__main__":
	main(sys.argv)
