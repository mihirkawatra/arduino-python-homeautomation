import sys
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM


SERVER_IP = '192.168.43.80'
PORT_NUMBER = 4500
SIZE = 1024
print("Test Client sending packets to IP {0}, via port {1}\n".format(SERVER_IP,PORT_NUMBER))

mysocket = socket(AF_INET,SOCK_DGRAM)
myMessage = "Hello!"
myMessage1 = "Shreyas"
i=0
while i<5:
	mysocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
	i=i+1
mysocket.sendto(myMessage1.encode('utf-8'),(SERVER_IP,PORT_NUMBER))

sys.exit()