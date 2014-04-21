from PySide import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import sys,os,csv

import numpy as np


# import pyuic generated user interface file
import template

app = QtGui.QApplication(sys.argv)


def fitregion():
	minX, maxX = myapp.region.getRegion()
	a = startpos = 0
	endpos = len(myapp.x)-1
	while a<len(myapp.x):
		if(myapp.x[a]<=minX):startpos = a
		if(myapp.x[a]>=maxX):
			endpos = a
			break
		a+=1
	avg = np.average(myapp.dIdV[startpos:endpos])
	return avg

class MyMainWindow(QtGui.QMainWindow, template.Ui_MainWindow):
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)
		self.c1col=(250,200,50)
		self.c2col=(250,200,250)
		self.c3col=(20,230,50)
		self.fitcol=(255,10,10)
		
		self.ready = False
		self.x = []
		self.y = []
		self.dIdV = []
		self.end = 0

		self.graph.setLabel('left', 'differential resistance', units='.')
		self.graph.setLabel('bottom', 'Voltage', units='V')

		self.editedgraph.setLabel('left', 'differential Conductance', units='.')
		self.editedgraph.setLabel('bottom', 'Voltage', units='V')

		self.region = pg.LinearRegionItem()
		self.region.setZValue(10)
		self.editedgraph.addItem(self.region)
		self.region.sigRegionChanged.connect(self.get_average_conductance)

		self.gc = self.editedgraph.plot()
		self.gc.setPen(self.c1col)


		self.c = self.graph.plot()
		self.c.setPen(self.c1col)

		self.load()

	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Escape:
			self.close()

		elif e.key() == QtCore.Qt.Key_Down:
			self.files.setCurrentIndex(self.files.currentIndex()+1)
		elif e.key() == QtCore.Qt.Key_Up:
			i=self.files.currentIndex()-1
			self.files.setCurrentIndex(i if i>=0 else 0)

		elif e.key() == QtCore.Qt.Key_Delete:
			os.remove(self.filename)
			self.files.removeItem(self.files.currentIndex())


	def get_average_conductance(self):
		try:
			val = fitregion()
			self.dIdVval.setText('%e'%(val ))
			self.dVdIval.setText('%e'%(1/val))
			self.normalize()		
		except:
			print 'loading...'
			
	def normalize(self):
		val = fitregion()
		self.gc.setData(self.x,self.dIdV/val)
		
		
	def load(self):
		allfiles = os.listdir('.')
		textfiles = [a for a in allfiles if a.split('.')[-1] == 'txt']
		textfiles.sort()
		self.files.addItems(textfiles)
	
	def loadfile(self,filename):
		if not filename == 'load file':
			try:		
				ar = np.loadtxt(filename)
				self.c.clear()
				self.gc.clear()
				self.x =np.concatenate(ar[:,0:1])
				self.y =np.concatenate(ar[:,1:2])
			except:
				print filename
			
			self.c.setData(self.x,self.y)
			self.dIdV = 1.0/self.y
			s=self.x.min()
			e=self.x.max()
			n=s+(e-s)/5.0
			self.region.setRegion([s,n])
			self.gc.setData(self.x,self.dIdV)
			self.ready = True
			

	def __del__(self):
		print 'BYE BYE'
			

		
myapp = MyMainWindow()


myapp.show()
app.exec_()


