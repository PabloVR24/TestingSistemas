import sys
import os

sys.stdin
class masaCorporal():
	def masaCORP(self):
		self.masa=[]
			for x in self.masa:
				if x <= 0:
					return "error"
				else:
					mc =float( self.masa[0] / ( self.masa[1] * self.masa[1] ))
					archivo = open("imc.txt","r+")
					archivo.write("%.2f" % mc)
		


if __name__ == '__main__':
	entrada= list(map(float, input().strip().split(' ')))
	for x in entrada:
		if x <= 0:
			return "error"

	main()

