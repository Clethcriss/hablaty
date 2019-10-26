import requests 
import keyboard
import threading, time
import sys
from pynput.keyboard import Key, Listener


def breakPrinter():
	global shouldSlowdown
	while True:
		print("Is breaking ", shouldSlowdown)
		time.sleep(3)


SPEEDCONTROLLURL = "http://192.168.0.180/motor?params="
HORNCONTROLLURL = "http://192.168.0.180/buzzer?params="
MAXSPEED = "1023"
actualSpeed = 0
shouldSlowdown = False

t1 = threading.Thread(target=breakPrinter)
t1.daemon = True
t1.start()

def on_press(key):
	global actualSpeed
	global SPEEDCONTROLLURL
	global HORNCONTROLLURL
	global shouldSlowdown
	if key == Key.right:
		if (actualSpeed + 100 < 1024):
			actualSpeed += 100
		else:
			actualSpeed = 1023
		print("Setting speed to: " + str(actualSpeed))
		try:
			requests.post(SPEEDCONTROLLURL + str(actualSpeed),timeout=1)  
		except:
			print("Something went wrong during speed setting")
	if key == Key.left:
		if actualSpeed - 100 > -1:
			actualSpeed -= 100
		else: 
			actualSpeed = 0
		print("Setting speed to: " + str(actualSpeed))
		try:
			requests.post(SPEEDCONTROLLURL+ str(actualSpeed),timeout=1)  
		except:
			print("Something went wrong during speed setting")
	if key == Key.space:
		shouldSlowdown = True
		try:
			requests.post(SPEEDCONTROLLURL+"0",timeout=1)
		except:
			print("exception caught")
	elif key == Key.up:
		try:
			shouldSlowdown = False
			requests.post(SPEEDCONTROLLURL+MAXSPEED,timeout=1)
			print("hi")
		except:
			print("exception caught")
	elif key == Key.caps_lock:
		try:
			requests.post(HORNCONTROLLURL+"104",timeout=1)
			print("caps down")
		except:
			print("excephellotion caught")        
												
def on_release(key):
	global shouldSlowdown
	print("")
	if key == Key.esc: 
		# Stop listener
		sys.exit()
		return False
	if key == Key.space:
		shouldSlowdown = False

with Listener(                                          
		on_press=on_press,
		on_release=on_release) as listener:
	listener.join()
