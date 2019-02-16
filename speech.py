import speech_recognition as sr  
import socket
import time

localIP     = "192.168.225.83"
localPort   = 20019
bufferSize  = 1024
msgFromServer       = "Hello Client"


UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("Server up and listening")

bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
message = bytesAddressPair[0]
address = bytesAddressPair[1]
clientMsg = "Message from Client:{}".format(message)
clientIP  = "Client IP Address:{}".format(address)
print(clientMsg)
print(clientIP)
# get audio from the microphone                                                                       
r = sr.Recognizer()
data = ""                                                                                
with sr.Microphone() as source:                                                                       
    print("Now you can Speak : ")
    print("\tListening.....")                                                                                
    audio = r.listen(source)
    print("\tProcessing.....")

#Processing the data.
try:
    data = r.recognize_google(audio)
    print("\nYou said:" + data)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

#Defining noise less enities.
nl_entity = ["FAN","LIGHT","DOOR","TEMPERATURE","ON","OFF","OPEN","CLOSE","ALL"]
noise = [".","'",",","!","?"]

def clean_nl_entity(data):
	words = data.split()
	nl_words=[word for word in words if word in nl_entity]
	nl_text=" ".join(nl_words)
	return nl_text

#Normalizing the data given.
data = data.upper()
txt = (((((data).upper()).replace(".","")).replace("!","")).replace("?","")).replace(",","")
nl_data = clean_nl_entity(txt)
print(nl_data)
def open(nl_data):
	nl = nl_data.split()
	if((nl[0]=="LIGHT" or nl[0]=="ON") and (nl[1]=="ON" or nl[1]=="LIGHT")):
		msg = "on"
		bytesToSend = str.encode(msg)
		UDPServerSocket.sendto(bytesToSend, address)
	elif((nl[0]=="LIGHTS" or nl[0]=="OFF") and (nl[1]=="OFF" or nl[1]=="LIGHTS")):
		msg = "off"
		bytesToSend = str.encode(msg)
		UDPServerSocket.sendto(bytesToSend, address)
	elif((nl[0]=="FAN" or nl[0]=="ON") and (nl[1]=="ON" or nl[1]=="FAN")):
		msg = "fan_on"
		bytesToSend = str.encode(msg)
		UDPServerSocket.sendto(bytesToSend, address)
	elif((nl[0]=="FAN" or nl[0]=="OFF") and (nl[1]=="OFF" or nl[1]=="FAN")):
		msg = "fan_off"
		bytesToSend = str.encode(msg)
		UDPServerSocket.sendto(bytesToSend, address)
	elif((nl[0]=="ALL" or nl[0]=="ON") and (nl[1]=="ON" or nl[1]=="ALL")):
		msg = "all_on"
		bytesToSend = str.encode(msg)
		UDPServerSocket.sendto(bytesToSend, address)
if (len(nl_data)!=0):
	open(nl_data)
else:
	print("")
UDPServerSocket.close()
