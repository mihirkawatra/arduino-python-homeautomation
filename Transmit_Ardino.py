import serial
k = str("")
response = str("")
def transmit(msg):
	ser = serial.Serial('com4',9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
	if(msg=="on" or msg == "three"):
		k = "on"
	elif(msg=="off"):
		k="off"
	elif(msg=="fan_on"):
		k="fan_on"
	elif(msg=="fan_off"):
		k="fan_off"
	elif(msg=="all_on"):
		k="all_on"
	elif(msg=="all_off"):
		k="all_off"
	for i in range(0,5):
		ser.write(k.encode())
		response = ser.readline().strip().decode("utf-8")
	print("Response: "+response)
	ser.close
transmit("all_off")