import socket               

s = socket.socket()         # Create a socket object
host = '192.168.43.87'    #private ip address of machine running fedora
port = 1023                
s.bind((host, port))       

s.listen(5)                
c, addr = s.accept()       
print ('Got connection from', addr)   #this line never gets printed
while True:
   data=c.recv(1023)
   print ("From Client: ", data)

c.close()  
