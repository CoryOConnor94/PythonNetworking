#!/usr/bin/env python3

"""Program takes user inputted domain name and returns IP address' associated
Usage: chmod +x to make executable
Usage Example: ./iplookup.py <domain-name>
"""
import socket
import sys
def main(argv):
	if len(argv) != 2:
		print("USAGE: iplookup <remote name>")
		
	else:
		remote_host = argv[1]
		ipList = socket.gethostbyname_ex(remote_host)
		print("{}".format(ipList))
		
		
if __name__ == "__main__":
	main(sys.argv)

