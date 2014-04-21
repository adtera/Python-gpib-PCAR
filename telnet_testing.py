
from anc300 import *
from keithley6221 import *

NP1 = ANC300()
print NP1.connect()

PD = KEITHLEY6221()
PD.connect()
PD.arm_PD()
#print NP1.go('echo off')
#print NP1.go('setf 1 1000')
#print NP1.go('setv 1 25')
#print NP1.go('getv 1')


#print NP1.go('stepd 1 5')
#print NP1.go('stepw 1')
#print NP1.go('stepu 1 5')

