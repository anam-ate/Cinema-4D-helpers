
import socket



UDP_IP = "172.16.100.61"
UDP_PORT = 7865	



#each finger is linked to each row
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
sock.close()