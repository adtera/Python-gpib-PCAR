import Gpib,time,string


class Lockin():
	def __init__(self):
		self.device=Gpib.Gpib('lockin')
	def write(self,cmd):
		self.device.write(cmd)
	def read(self,bytes):
		self.device.read(bytes)
	def clear(self):
		self.device.clear()
