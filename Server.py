from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys

PORT = 4500
SIZE = 1024

hostname = gethostbyname( '0.0.0.0' )
mysocket = socket( AF_INET, SOCK_DGRAM )
mysocket.bind( (hostname, PORT) )

print("Test server Listening on Port {0}\n".format(PORT))

while True:
	(data,addr) = mysocket.recvfrom(SIZE)
	print(data)
sys.exit()