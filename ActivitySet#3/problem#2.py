
class complex:
	def __init__(self,real,imag):
		self.real=real
		self.imag=imag
	def getdata(self):
	          print("{0}+{1}j".format(self.real,self.imag))
  
c1=complex(4,6)
c1.getdata()
