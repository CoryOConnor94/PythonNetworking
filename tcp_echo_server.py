#!/usr/bin/env python3
"""TCP server receives message from client and echos message back
Usage: chmod +x to make executable
Usage Example: ./tcp_echo_server.py
"""
import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def socket_setup():
    """Set up socket to listen for connection on bound IP and Port"""
    server_port = 6060
    socket_addr = ("", server_port)
    server_sock.bind(socket_addr)
    server_sock.listen(1)


def connect_to_client():
    """Accept connection from client, receive message, and return message to client"""
    while True:
        print("Waiting for client to connect")
        connect_sock, addr = server_sock.accept()
        data = connect_sock.recv(50000)
        decode_data = data.decode()
        print(f"Client: {decode_data}")
        to_client = decode_data + " Back to you!"
        to_client_bytes = to_client.encode("UTF-8")
        connect_sock.sendall(to_client_bytes)
        connect_sock.close()


def main():
    socket_setup()
    connect_to_client()


if __name__ == "__main__":
    main()
