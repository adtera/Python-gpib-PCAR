#Commands for dealing with the KEITHLEY 6221,2182a

import Gpib, time, socket, threading
import os,string
import numpy as np

from console_out import *

class KEITHLEY6221:
	def __init__(self,start=-2e-3,stop=2e-3,pts = 100,width=100e-6,nanorange=1):
		self.host    = 'acdcsource'	#GPIB mnemonic for KEITHLEY 6221
		self.timeout = 30
		self.status=''
		self.identity=''
		self.connected=False
		self.error_buffer = []
		
		self.armed=False
		self.start_current = start
		self.stop_current = stop
		self.pts = pts
		self.stepsize =0
		self.set_stepsize()
		self.data_stream=''

		self.DC_delta = self.stepsize*2

		self.voltage_compliance=nanorange
		self.pulse_width = width


		self.progress = 100
		self.filenumber = 0
		self.filename = 'default'
		self.received_points=0
		
		self.style='\033[7;95m'
		self.text=Text()
		self.communicationLock = threading.Lock()		


	def connect(self):
		try:
			self.device = Gpib.Gpib(self.host)
			self.identity = self.go('*IDN?')
			self.text.show(self.identity,'message')
			self.status	=	'connected'
			self.connected = True
			self.identity = self.go('*RST')
			time.sleep(1)
			self.go(':TRAC:CLE')

		except socket.timeout:
			self.status = "socket timeout"
			self.identity = 'none'
			self.connected = False
		return self.identity
		
	def go(self,command):
		self.communicationLock.acquire()
		self.device.write(command)
		if '?' in command:
			received = self.device.read(1000).split('/700x')[0]
			self.communicationLock.release()
			#print received
			self.text.show(command+':'+received[:-10]+'...','blue')
			return received.strip()
		else:
			self.text.show(command+':'+'\t\t|','blue')
			self.communicationLock.release()
			return True
		
	def clear(self):
		self.go('*CLS')
	
	def get_errors(self):
		err = self.go('STAT:QUE:NEXT?')
		if(len(err)>2):
			print err.split(',')
			#num,msg = err.split(',')
			#if(num!='0'):
			#	self.error_buffer.append([num,msg] )
			#print self.error_buffer


	def init_measurements(self):
		if self.status:
			self.filenumber = 0
			self.clear()
			self.go(':TRAC:CLE')
			self.go('*CLS')
			self.progress = 0
			self.x_axis=[]
			self.y_axis=[]
			self.received_points=0
			self.data_stream=''
			self.go('INIT:IMM')
			self.filename = time.strftime('%d-%h_%H-%M')
			self.file = open('data/'+self.filename+'.txt','wt')

	def abort(self):
			''' disarm and return to normal state'''
			self.text.show('Disarming ...','message')
			self.go("SOUR:SWE:ABOR")
			time.sleep(1)
			self.armed=False

	def get_status(self):
			#if int(self.go('SOUR:DCON:ARM?')) : self.armed = 'DC'
			#if int(self.go('SOUR:PDEL:ARM?')) : self.armed = 'PD'
			return self.armed

	def set_stepsize(self):
		self.stepsize = abs(self.stop_current - self.start_current)/self.pts
		self.DC_delta = self.stepsize*2
		if(self.stepsize<1e-7): self.stepsize = 1e-7
		self.DC_delta = self.stepsize*2


	def get_datapoints(self):
		if self.status:
			recv = 	self.received_points

			try:
				total_points =int( self.go(':TRAC:POIN:ACT?') )
			except:
				print 'failed to estimate points'
				return [[],[]]
			print 'stored points ',total_points
			if(total_points>5):
				pts = 50 if 50<(total_points-recv) else (total_points-recv)
				print ' fetching points from ',recv,' to ',recv+pts
				self.data_stream=self.go(':TRAC:DATA:SEL? %d,%d'%(recv,pts ))
				data=self.data_stream.split(',')
				if len(data) > 4:
					n=0
					print data[0],data[1]
					recent_points=[]
					try:
						while n<len(data)-2:
							y=float(data[n])
							x=float(data[n+1])
							recent_points.append([x,y])
							self.file.write('%e %e\n'%(x,y))
							self.received_points+=1
							if y<1 and x <1:	#FIX THIS LATER!!!!!!!!
								self.x_axis.append( x )
								self.y_axis.append( y )
							n+=2
					except:
						f = open('errorfile.err','wt')
						f.write(self.data_stream)
						print 'some error just happened'
						f.close()
					self.progress = round((self.received_points*100)/(self.pts))
					if self.armed == 'DC':
						return self.x_axis,self.y_axis
					elif self.armed =='PD': # We need to calculate dIdV
						I=np.array(self.y_axis)
						V=np.array(self.x_axis)
						dI = np.diff(I)
						dV = np.diff(V)
						j=V[:-1]	# remove last element since Y axis will lose one too
						sorter = j.argsort()
						k=dI/dV
						k=k[sorter]
						j=j[sorter]
						infinities = np.where(k==np.inf)[0]
						j=np.delete(j,infinities)
						k=np.delete(k,infinities)
						return V,I


		else:
			self.text.message(' not initialized','error',self.name+'  ',self.style)
		return [[],[]]

	'''
	def get_datapoints(self):
		if self.status:
			recv = len(self.x_axis)
			total_points =int( self.go(':TRAC:POIN:ACT?') )
			print 'stored points ',total_points
			if(total_points>5):
				pts = 50 if 50<(total_points-recv) else (total_points-recv)
				print ' fetching points from ',recv,' to ',recv+pts
				self.data_stream=self.go(':TRAC:DATA:SEL? %d,%d'%(recv,pts ))
				data=self.data_stream.split(',')
				if len(data) > 4:
					n=0
					print data[0],data[1]
					while n<len(data)-2:
						self.x_axis.append( float(data[n]) )
						self.y_axis.append( float(data[n+1]) )
						n+=2
					self.progress = round((len(self.x_axis)*100)/(self.pts))
					if self.armed == 'DC':
						return self.x_axis,self.y_axis
					elif self.armed =='PD': # We need to calculate dIdV
						I=np.array(self.y_axis)
						V=np.array(self.x_axis)
						dI = np.diff(I)
						dV = np.diff(V)
						j=V[:-1]	# remove last element since Y axis will lose one too
						sorter = j.argsort()
						k=dI/dV
						k=k[sorter]
						j=j[sorter]
						infinities = np.where(k==np.inf)[0]
						j=np.delete(j,infinities)
						k=np.delete(k,infinities)
						return k,j


		else:
			self.text.message(' not initialized','error',self.name+'  ',self.style)
		return [[],[]]

	'''

#-----------------------------------------------DIFFERENTIAL CONDUCTANCE----------------------------------------------

	def arm_DC(self):
		if self.status:
			self.go('SYST:COMM:SER:SEND "VOLT:NPLC 1"')
			self.go(':syst:comm:ser:send ":sens:volt:rang %s"'%(str(self.voltage_compliance))) 
			time.sleep(0.5)
			rep = self.go('SOUR:DCONductance:NVPResent?')
			self.text.show('Serial connection check[dI/dV] :'+rep,'message')
			self.clear()
			self.set_DC_start_current()
			self.set_DC_stop_current()
			self.set_DC_stepsize()
			self.set_DC_delta()
			self.set_DC_delay()

			self.go('SOUR:SWE:RANG BEST')
			self.go(':FORM:ELEM AVOL,READ')
			self.go('SOUR:PDEL:LME 1')
			self.go(':TRAC:CLE')

			self.go('SOUR:DCON:ARM')
			time.sleep(1)
			self.armed = 'DC'
			self.get_errors()

	def set_DC_start_current(self):
			self.go('SOUR:DCON:STARt %e'%(self.start_current))

	def set_DC_stop_current(self):
			self.go('SOUR:DCON:STOP %e'%(self.stop_current))

	def set_DC_stepsize(self):
			self.go('SOUR:DCON:STEP %e'%(self.stepsize))

	def set_DC_delta(self):
			self.go('SOUR:DCON:DELTa %e'%(self.DC_delta))

	def set_DC_delay(self):
			self.go('SOUR:DCON:DELay 1E-1')
			
#|||||||||||||||||||||||||||||||------------DIFFERENTIAL CONDUCTANCE----------||||||||||||||||||||||||||||

		
			

#-----------------------------------------------PULSED DELTA----------------------------------------------
	def arm_PD(self):
		
		if self.status:
			self.go('SYST:COMM:SER:SEND "VOLT:NPLC 1"') #to nanovoltmeter
			self.go(':syst:comm:ser:send ":sens:volt:rang %s"'%(str(self.voltage_compliance))) 
			time.sleep(0.5)
			self.go('SOUR:PDEL:WIDT %e'%(self.pulse_width))
			self.sdel = self.pulse_width/2.0  
			if(self.sdel<55e-6): self.sdel = 55e-6 # so that it is always > 55uS
			self.go('SOUR:PDEL:SDEL %e'%(self.sdel)) #source delay. (settling time)
			
			self.go('SOUR:PDEL:INT 5')    

			
			self.go('SOUR:PDEL:SWE ON')   
			self.go('SOUR:SWE:SPAC LIN')

			self.set_PD_start_current()
			self.set_PD_stop_current()
			self.set_PD_stepsize()
			self.set_PD_delay()


			self.go('SOUR:SWE:RANG BEST')
			self.go(':FORM:ELEM READ,SOUR')
			self.go('SOUR:PDEL:LME 1')
			self.go(':TRAC:CLE')
			self.text.show('Arming Pulse Delta ','message')
			self.go('SOUR:PDEL:ARM')
			time.sleep(2)
			self.armed = 'PD'
			
	def set_PD_start_current(self):
			self.go('SOUR:CURR:STARt %e'%(self.start_current))

	def set_PD_stop_current(self):
			self.go('SOUR:CURR:STOP %e'%(self.stop_current))

	def set_PD_stepsize(self):
			self.go('SOUR:CURR:STEP %e'%(self.stepsize))

	def set_PD_delay(self):
			self.go('SOUR:DEL 1e-1')

		


#|||||||||||||||||||||||||||||||||||||------------PULSED DELTA----------||||||||||||||||||||||||||||||||||||||||||


#-----------------------------------------------CONTINUOUS DELTA----------------------------------------------
	def arm_delta(self):
		
		if self.status:
			self.go('pdel:high 1e-3')
			self.go('pdel:coun INF') 
			self.go('pdel:widt 1e-4') 
			self.go('pdel:sdel 6e-5') 
			self.go('sour:del 100e-3') 
			self.go('SOUR:PDEL:INT 5')    
			self.go(':syst:comm:ser:send ":sens:volt:rang %s"'%(str(self.voltage_compliance))) 

			
			self.go('pdel:arm')
			time.sleep(3)   
			self.go(':init:imm')

			self.go(':TRAC:CLE')
			self.text.show('Arming Delta ','message')
			self.armed = 'delta'
			
	def get_latest(self):
		if self.status:
			return self.go(':SENS:DATA:LAT?')


#|||||||||||||||||||||||||||||||||||||------------CONTINUOUS DELTA----------||||||||||||||||||||||||||||||||||||||||||




	def nvpr(self):
			try:
				return int(self.go('SOUR:DCONductance:NVPResent?'))
			except:
				return 0





	def to_file(self):
		f=open('pd.txt','wt')
		for n in self.points:
			f.write('%s %s\n'%(n[0],n[1]) )
		print 'written to file'
		f.close()

