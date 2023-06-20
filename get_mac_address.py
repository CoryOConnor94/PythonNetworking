#!/usr/bin/env python3
"""Returns MAC address of given interface
Usage: chmod +x to make executable
Usage Example: ./get_mac_address.py <interface name>
"""

from socket import socket, AF_PACKET, SOCK_RAW
import sys


def get_mac(interface_name):
    """Extracts MAC address as bytes, converts to HEX and displays result"""
    raw_sock = socket(AF_PACKET, SOCK_RAW)
    port = 0
    raw_sock.bind(interface_name, port)
    sock_name = raw_sock.getsockname()
    mac_address = sock_name[4].hex(":")
    raw_sock.close()
    print(f"The MAC address of {interface_name} is {mac_address}")


def main():
    try:
        get_mac(sys.argv[1])
    except IndexError:
        print("IndexError\nUsage: ./get_mac_address.py <Interface name>")
        exit()


if __name__ == "__main__":
    main()
