
# Date : 01.01.2022


# Encapsulation -> class = charcteristics + behaviour
# class defination
class Arithmetic:
	def __init__(self,a,b):                 # constructor
		print("Inside init (Constructor)")
		self.no1 = a                        # characteristics
		self.no2 = b                        # characteristics

	def Addition(self):                     # behaviour
		ans = self.no1 + self.no2
		return ans



def main():
	print("Enter first Number : ")
	x = int(input())

	print("Enter second Number : ")
	y = int(input())

	obj = Arithmetic(x,y)                 # object creation
	ret = obj.Addition()
	
	print("Addition is : ",ret)

if __name__ == "__main__":
	main()


