"""
polymorphisom (method overloading)
there is no such a concept like method overloading in python 

Date : 09.01.2022
"""

class Demo:
	def __init__(self):
		self.i = 10
		self.j = 20
	
	def Add(self,a):     # method
		print("Inside add with one parameter")
	
	def Add(self,a,b):  # overloaded method
		print("Inside add with two paramters")


def main():
	obj = Demo()
	obj.Add(11)
	obj.Add(11,21)


if __name__ == "__main__":
	main()


