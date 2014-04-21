#Commands for dealing with the ANC300 controller

import telnetlib, time, socket

class ANC300:
	def __init__(self):
		self.host    = '192.168.10.3'	#IP address for ANC300
		self.port	= 7230			#standard telnet console port.  LUA console is at 7231
		self.timeout = 30
		self.password='123456'
		self.status=''
		self.identity=''
		self.connected=False

	def connect(self):
		start_time=time.time()
		try:
			self.session = telnetlib.Telnet(self.host, self.port, self.timeout)
			print time.time()-start_time
			self.identity = self.session.read_until('code: ', 2 ).split('Authorization')[0]
			print time.time()-start_time
			self.session.write(self.password+'\r\n')		#send default password
			print time.time()-start_time
			print self.session.read_lazy()
			self.status	=	'connected'
			self.connected = True
		except socket.timeout:
			self.status = "socket timeout"
			self.identity = 'none'
			self.connected = False
			
		return self.identity
		
	def go(self,command):
		self.session.write(command+'\r\n')
		if(command[:3]=='get'):
			received = self.session.read_until('OK', 2 )
		else:
			received = 'Done'
		return received.split('OK')[0]
