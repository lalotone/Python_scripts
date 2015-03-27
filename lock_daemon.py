import bluetooth
import time
import os
#you'll need to install xdotool with sudo apt-get install xdotool
bd_addr = "00:00:00:00:00:00"#here the mac
connected = False
condicion = True
contador = 0

def isAlive():
	print("Connecting...")
	result = bluetooth.lookup_name(bd_addr, timeout=5)
	if (result != None):
		print("Connected")
		return True
	else:
		return False

while condicion == True:
	if(isAlive() == True):
		print("Target acquired")
		os.system("gnome-screensaver-command -d")
		time.sleep(1)
		if contador == 0:
			os.system("xdotool type yourpasshere && xdotool key Return")#here the pass
			contador = contador + 1 
	else:
		print("Target lost")
		os.system("gnome-screensaver-command -l")
		contador = 0
		
