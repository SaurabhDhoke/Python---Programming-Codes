# Date : 01.01.2022

class Demo:
	A = 10    # class Variable
	
	def __init__(self): 
		self.B = 30      # instance variable
	
	def fun(self):       # instance method
		print("Inside Instance method fun ")
	
	@classmethod    
	def gun(cls):       # class method
		print("Inside Class Method")
	
	
	
def main():
	print("Value of class variable : ",Demo.A)
	Demo.gun()
	obj1 = Demo()
	obj1.gun()       # class methode obj ni pn call karata yete
	
	print("Value of instance variable : ",obj1.B)
	obj1.fun()
	
if __name__ == "__main__":
	main()


































