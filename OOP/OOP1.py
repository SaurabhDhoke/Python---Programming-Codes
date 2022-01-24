
# Date : 01.01.2022

class Arithmetic:
	def __init__(self,a,b):                 
		print("Inside init (Constructor)")
		self.no1 = a                       
		self.no2 = b                      

	def Addition(self):      # self == this keyword               
		ans = self.no1 + self.no2
		return ans
		

def main():
	obj1 = Arithmetic(10,11)                
	ret = obj1.Addition()       # Addition(obj1)    Addition(0x100)
	print("Addition is : ",ret)

	obj2 = Arithmetic(20,21)                
	ret = obj2.Addition() 		# Addition(obj2)    Addition(0x200)
	print("Addition is : ",ret)


if __name__ == "__main__":
	main()


