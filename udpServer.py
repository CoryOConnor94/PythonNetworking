#!/usr/bin/env python3 
# udpserver.py 
import socket             # socket(), bind(), sendto(), recvfrom()  
 
def udpserver(host, port): 
    BUFSIZE = 512 
 
    # STEP 1 - Create socket for data from a client  
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
 
    # STEP 2 - Bind socket to socket address      
    serverAddr = ( host, port )    # 2-tuple for server address info   
    sock.bind(serverAddr) 
     
    # STEP 3 - Repeatedly communicate with UDP clients    
    while True:  # loop forever    
        print("Waiting for data from a client on port", port)   
 
        # Receive message from client    
        data, address = sock.recvfrom(BUFSIZE) 
     
        print("received {} bytes from {}".format(len(data), address)) 
        print(data.decode()) 

     
        if data: 
            sent = sock.sendto(data, address) 
            print("sent {} bytes back to {}".format(sent, address)) 
 
if __name__=="__main__": 
    udpserver("", 6060) 
