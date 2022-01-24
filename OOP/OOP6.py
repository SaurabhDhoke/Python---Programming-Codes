"""
Date : 02.01.2022
"""

class Demo:
	A = 10               
	def __init__(self):
		print("Inside Constructor")
		self.B = 20      
	
	def fun_instance(self):		
		print("Inside Instance Methode")
		print(self.B)
		print(self.A)	# try to avoid this
		print(Demo.A) 	# this is the correct way to access the class variable
		
	@classmethod
	def fun_class(cls):		  
		print("inside Class Method")
		print(cls.A)
		print(Demo.A)  # both are same
		# print(cls.B)   he chalat nahi
		
		
	@staticmethod
	def fun_static():       
		print("inside static method")
		print(Demo.A)
		# print(Demo.B)  not Allowed
		
	def __del__(self):
		print("Inside Destructor")
		
def main():
	
	# obj = Demo()  # object creation
	# obj.fun_instance()
	# obj.fun_class()
	
	Demo.fun_static()
	
	
	
if __name__ == "__main__":
	main()























