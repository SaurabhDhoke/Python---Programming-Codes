"""
abstraction ( __ )
hide variable (private)

Date : 02.01.2022
"""

class Demo:
	def __init__(self):
		self.A = 10    # public variable of class
		self.__B = 20  # private variable of class  (abstraction)
	
	def fun(self):
		print("inside fun")
		print(self.A)
		print(self.__B)
			

def main():
	obj = Demo()
	print(obj.A)
	obj.fun()
	#print(obj.__B)  # you cant access private variable outside the class 

if __name__ == "__main__":
	main()


# A is a public variable
# B is a private variable 
# private karanya sathi variable chya adhi __ dyav lagat 

















