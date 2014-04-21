import time
from keithley6221 import *

a =  KEITHLEY6221(1e-4,1e-4,1,400e-6,1)
a.connect()
a.arm_delta()
for l in range(5):
	time.sleep(1)
	print a.get_latest()
