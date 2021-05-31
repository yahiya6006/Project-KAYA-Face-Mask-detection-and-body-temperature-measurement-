# In this program we are going to read the data from the arduino
import serial
import struct

baudRate = 19200
comPort = "COM13"

try:
	port = serial.Serial(comPort, baudRate)
	port.flushInput()
except serial.serialutil.SerialException:
	print('[INFO] Arduino is not connected.')

#----- in this function we will take the data from arduino -------------
def Temperature():
	# we will return the average of 3 readings
	port.flushInput()
	while(port.isOpen()):
		read_data = port.readline()
		try:
			val = read_data[0:len(read_data)-2].decode("utf-8")
		except UnicodeDecodeError:
			continue
		try:
			val = float(val)
		except ValueError:
			continue
		if val <= 25 and val >= 50:
			return 0
		return val
		
if __name__ == "__main__":
	for _ in range(30):
		temp = GetSerialData()
		print(temp)