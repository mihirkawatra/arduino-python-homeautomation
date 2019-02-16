import socket
import Transmit_Ardino

msgFromClient       = "Client 1 Available. "
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("192.168.43.86", 20018)
bufferSize          = 1024
print("Client Active")
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("Client trying to Connect to server.")
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
print("Client Connected")
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = msgFromServer[0]
msg = msg.decode("utf-8")
print(type(msg))

if(msg == ""):
	print("No message Received from Client.")
else:
	print(msg)
UDPClientSocket.close()
Transmit_Ardino.transmit(msg)