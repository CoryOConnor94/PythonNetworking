#!/usr/bin/env python3 
# udpclient.py 
import socket             # socket(), bind(), sendto(), recvfrom()  
 
def runclient(servHost, servPort): 
    BUFSIZE = 512 
 
    # STEP 1 - Create socket for data to/from server  
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
 
    # 2-tuple for server address info   
    serverAddr = ( servHost, servPort ) 
  
    message = 'This is the message to be sent and received' 
 
    try: 
        # STEP 2 - Send datagram 
        print("sending: ", message) 
        sock.sendto(message.encode(), serverAddr) 
 
        # STEP 3 - Receive response 
        print("waiting to receive") 
        data, server = sock.recvfrom(BUFSIZE) 
        print("received: ", data.decode()) 
 
    except OSError as err: 
        print("Error {}".format(err)) 
 
    finally: 
        # STEP 4 – close socket 
        print("closing socket") 
        sock.close() 
 
if __name__=="__main__": 
    runclient("localhost", 6060)
