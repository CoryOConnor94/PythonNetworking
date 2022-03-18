#!/usr/bin/env python3

"""Program takes user inputted domain name returns all IPv4 and IPv6 address' on port 80
Usage: chmod +x to make executable
Usage Example: ./dnsLookUp.py google.com
"""
import socket

domain = input("Enter Website: ")
port = 80
try:
	addrinfo = socket.getaddrinfo(domain, port)
	ipList = [field[-1][0] for field in addrinfo]
	print("IP Addresses for: ", domain)
	for ip in set(ipList):
		print(ip)
except socket.gaierror as e:
	print("Get Address Info Error >> ",e)
	
