#!/usr/bin/env python3
"""TCP client sends message to TCP server and receives message back from server
Usage: chmod +x to make executable
Usage Example: ./tcp_echo_client.py <message here>
"""
import sys
import socket

server_ip = "127.0.0.1"
server_port = 6060
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_addr = (server_ip, server_port)


def send_message(message):
    """Sends Message to listening server"""
    client_sock.connect(sock_addr)
    msg_bytes = message.encode("UTF-8")
    client_sock.sendall(msg_bytes)


def receive_message():
    """Receives message back from server"""
    data = client_sock.recv(1024)
    decoded_data = data.decode()
    print(f"Server: {decoded_data}")


def main():
    try:
        send_message(sys.argv[1])
    except IndexError:
        print("IndexError\nUsage: ./tcp_echo_client.py <Message here>")
        exit()
    receive_message()
    client_sock.close()


if __name__ == "__main__":
    main()
