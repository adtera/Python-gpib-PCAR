from PySide import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import sys,os,csv,random

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

		self.legendbox = pg.LegendItem((100,60), offset=(70,10))
		self.legendbox.setParentItem(self.graph.graphicsItem())
		
		self.editedgraph.setLabel('left', 'differential Conductance', units='.')
		self.editedgraph.setLabel('bottom', 'Voltage', units='V')

		self.region = pg.LinearRegionItem()
		self.region.setZValue(10)
		self.editedgraph.addItem(self.region)
		self.region.sigRegionChanged.connect(self.get_average_conductance)

		self.gc = self.editedgraph.plot()
		self.gc.setPen(self.c1col)

		self.cg2 = self.graph2.plot()
		self.cg2.setPen((255,255,255))
		self.exporter = pg.exporters.ImageExporter.ImageExporter(self.graph2.plotItem)
		self.exporter.parameters()['width'] = 300

		self.mainexporter = pg.exporters.ImageExporter.ImageExporter(self.graph.plotItem)
		self.mainexporter.parameters()['width'] = 1000

		self.c = self.graph.plot()
		self.c.setPen(self.c1col)
		self.textfiles=[]
		self.load()
		#self.loadthumbs()
		
		self.plots = []
		
	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Escape:
			self.close()

		elif e.key() == QtCore.Qt.Key_Down:
			self.files.setCurrentIndex(self.files.currentIndex()+1)
		elif e.key() == QtCore.Qt.Key_Up:
			i=self.files.currentIndex()-1
			self.files.setCurrentIndex(i if i>=0 else 0)

		elif e.key() == QtCore.Qt.Key_Delete:
			print 'deleting ',self.files.currentText()
			os.remove(self.files.currentText())
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
		self.textfiles = [a for a in allfiles if a.split('.')[-1] == 'txt']
		self.textfiles.sort()
		self.files.addItems(self.textfiles)
	
	
	def loadfile(self,filename):
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
			

	def generate_thumbnails(self):
		for f in self.textfiles:
			try:
				ar = np.loadtxt(f)
				self.x =np.concatenate(ar[:,0:1])
				self.y =np.concatenate(ar[:,1:2])
			except:
				print f

			self.cg2.setData(self.x,self.y)
			self.savethumb(f[:-4]+'.jpg'  )
		self.loadthumbs()

	def loadthumbs(self):
		allfiles = os.listdir('./thumbs')
		files = [a for a in allfiles if a.split('.')[-1] == 'jpg']
		files.sort()
		for f in files:
			x = QtGui.QIcon('./thumbs/'+f)
			a = QtGui.QListWidgetItem(x,f[:-4])
			self.thumbs.addItem(a)
		
	def plot_selection(self):
		self.c.clear()
		for a in self.plots:
			a.clear()
		self.plots= []
		self.legendbox.scene().removeItem(self.legendbox)
		self.legendbox = pg.LegendItem((100,60), offset=(70,10))
		self.legendbox.setParentItem(self.graph.graphicsItem())
		num = 0
		cols = [(255,0,0),(255,255,0),(255,0,255),(255,255,255),(0,255,0),(0,0,255),(0,255,255),(255,100,100),(100,255,100),(100,100,255)]
		for a in self.thumbs.selectedItems():
			if len(cols):
				col=cols.pop()
			else:
				r=random.random()*155+100
				g=random.random()*155+100
				b=random.random()*155+100
				col = (r,g,b,255)
			c = self.graph.plot()
			c.setPen(col,width=2)
			ar = np.loadtxt(a.text()+'.txt')
			x =np.concatenate(ar[:,0:1])
			y =np.concatenate(ar[:,1:2])
			c.setData(x,y)
			self.legendbox.addItem(c, a.text().split('_')[-1])
			num+=1
			if num>10:
				self.legendbox = pg.LegendItem((100,60), offset=(70,10))
				self.legendbox.setParentItem(self.graph.graphicsItem())
				num =0 				
			self.plots.append(c)


	def saveplot(self):
		filename = self.filename.text()+'.jpg'
		print 'saved to ' ,filename
		self.mainexporter.export(filename)


	def savethumb(self,filename):
		self.exporter.export('thumbs/'+filename)


	def __del__(self):
		print 'BYE BYE'
			

		
myapp = MyMainWindow()


myapp.show()
app.exec_()


