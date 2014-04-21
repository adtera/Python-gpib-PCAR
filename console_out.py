class Text:
	HEADER = '\033[1;95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[7;31m'
	ENDC = '\033[0m'
	types={'warning':WARNING,'error':FAIL,'message':HEADER,'blue':OKBLUE,'green':OKGREEN}
	def show(self,txt,tp):
		print self.types[tp] + txt + self.ENDC

	def message(self,txt,tp,name='',style='\033[1;95m'):
		print style + name + self.ENDC + self.types[tp] + txt + self.ENDC

	def bar(self):
		print '\033[42m' + '%'*27+'-'*27+'%'*26 + self.ENDC

