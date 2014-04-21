#Commands for dealing with the KEITHLEY 6221,2182a

import Gpib, time, socket, threading
import os,string
import numpy as np


from console_out import *

class MULTI:
	def __init__(self):
		self.host    = 'multi'	#GPIB mnemonic for Lakeshore temp controller
		self.timeout = 30
		self.status=''
		self.identity=''
		self.connected=False
		self.input_num = 'A'
		self.curve_num = 21
		self.selected_curve = ''
		self.style='\033[7;95m'
		self.val=''
		self.text=Text()
		self.communicationLock = threading.Lock()
		
	def connect(self):
		try:
			self.device = Gpib.Gpib(self.host)
			self.identity = self.go('*IDN?')
			self.text.show(self.identity,'message')
			self.status	=	'connected'
			self.connected = True

		except socket.timeout:
			self.status = "socket timeout"
			self.identity = 'none'
			self.connected = False
		return self.identity
		

	def go(self,command):
		self.communicationLock.acquire()
		try:
			self.device.write(command)
			received = self.device.read(100)#.split('\r\n')[0]
		except:
			received='0'
		self.communicationLock.release()
		return received.strip()
		
	def clear(self):
		self.go('*CLS')

	def get_val(self):
		#print self.input_num,len(self.input_num)
		self.val = self.go(':DATA?')
		return self.val
		

