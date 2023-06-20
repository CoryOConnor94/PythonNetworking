#!/usr/bin/env python3
"""Perform DNS lookup on given domain name
Usage: chmod +x to make executable
Usage Example: ./dnsLookUp.py google.com
"""
import socket
import sys

try:
    # DOMAIN = sys.argv[1]
    DOMAIN = "google.com"
    PORT = 80
    addr_info = socket.getaddrinfo(DOMAIN, PORT)
    ip_list = [field[-1][0] for field in addr_info]
    print(ip_list)
    print(f"IP Addresses for: {DOMAIN}")
    for ip in set(ip_list):
        print(ip)

except IndexError:
    print("IndexError\nUsage: ./dns_lookup.py <Domain name>")
    exit()

except socket.gaierror as e:
    print(f"Get Address Info Error >> {e}")




