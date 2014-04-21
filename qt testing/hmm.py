import sys,os

from PySide import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl

import numpy as np
# import pyuic generated user interface file
import template

from keithley6221 import *

PD = KEITHLEY6221()
PD.connect()
PD.arm_PD()


app = QtGui.QApplication(sys.argv)


def rand(n):
    data = np.random.random(n)
    data[int(n*0.1):int(n*0.13)] += .5
    data[int(n*0.18)] += 2
    data[int(n*0.1):int(n*0.13)] *= 5
    data[int(n*0.18)] *= 20
    data *= 1e-12
    return data, np.arange(n, n+len(data)) / float(n)
    
    
index = 0
def update():
	global z, index
	index -= 1
	myapp.p4.setData(z=myapp.z[index%myapp.z.shape[0]])
	yd, xd = rand(1000)

	
class MyMainWindow(QtGui.QMainWindow, template.Ui_MainWindow):
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)
		#self.c=Qwt5.QwtPlotCurve()
		#self.c.attach(self.plt)
		self.timer = QtCore.QTimer()
		self.timer.start(5.0)
		self.timer.timeout.connect(update) 
		self.qtgraph.setLabel('left', 'Voltage', units='V')
		self.qtgraph.setLabel('bottom', 'Current', units='A')
		self.c1 = self.qtgraph.plot()
		self.c1.setPen((200,200,100))


		## Add a grid to the 3D view
		g = gl.GLGridItem()
		g.scale(2,2,1)
		g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
		self.pyqt3d.addItem(g)



		## Animated example
		## compute surface vertex data
		cols = 90
		rows = 100
		self.x = np.linspace(-8, 8, cols+1).reshape(cols+1,1)
		self.y = np.linspace(-8, 8, rows+1).reshape(1,rows+1)
		d = (self.x**2 + self.y**2) * 0.1
		d2 = d ** 0.5 + 0.1

		## precompute height values for all frames
		phi = np.arange(0, np.pi*2, np.pi/20.)
		self.z = np.sin(d[np.newaxis,...] + phi.reshape(phi.shape[0], 1, 1)) / d2[np.newaxis,...]


		## create a surface plot, tell it to use the 'heightColor' shader
		## since this does not require normal vectors to render (thus we 
		## can set computeNormals=False to save time when the mesh updates)
		self.p4 = gl.GLSurfacePlotItem(x=self.x[:,0], y = self.y[0,:], shader='heightColor', computeNormals=False, smooth=True)
		self.p4.shader()['colorMap'] = np.array([0.2, 2, 0.5, 0.2, 1, 1, 0.2, 0, 2])
		#self.p4.translate(10, 10, 0)
		self.pyqt3d.addItem(self.p4)


		#self.v = gl.GLVolumeItem(d2)
		#self.v.translate(-50,-50,-100)
		#self.pyqt3d.addItem(self.v)

		ax = gl.GLAxisItem()
		self.pyqt3d.addItem(ax)

		#self.btn.clicked.connect(lambda: self.timer.setInterval(self.timer.interval()/2))

		#self.connect(self.timer, QtCore.SIGNAL('timeout()'), plotSomething) 
		#self.btn.clicked.connect(lambda: self.timer.setInterval(self.timer.interval()/2))
		# connect myaction_logic to myaction.toggled signal
		#self.myaction.toggled.connect(self.gogo)


	def start_measuring(self):
		print 'Measuring....'
		PD.init_measurements_PD()

	def read_buffer(self):
		I,V = PD.get_PD()
		print I
		print V
		self.c1.setData(I,V)

myapp = MyMainWindow()
myapp.show()
sys.exit(app.exec_())
