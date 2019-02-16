import serial
import socket

msgFromClient       = "Client 1 Available. "
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("192.168.255.192", 20017)
bufferSize          = 1024
print("Client Active.")
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "{}".format(msgFromServer[0])

print(msg)

if(msg == ""):
	print("No message Received from Client.")
else:
	print(msg)
UDPClientSocket.close()

ser = serial.Serial('com3', 9600)


while True :
    ser.write(message.encode())
    t2=ser.readline().strip().decode("utf-8")
    #print(t2)
print("done")
