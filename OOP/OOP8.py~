"""
abstraction ( __ )
hide method (private)

Date : 02.01.2022
"""

class Demo:
	def __init__(self):
		self.A = 10   
		self.__B = 20  
	
	def fun(self):		     # private method of a class
		print("inside fun")
		self.__gun()

	def __gun(self):
		print("inside gun")  # private method of a class		

def main():
	obj = Demo()
	obj.fun()
	# obj.gun()   # cant access private method outside the class

if __name__ == "__main__":
	main()


"""
 fun is a public method
 gun is a private method 
 private karanya sathi variable chya adhi __ dyav lagat 
"""
