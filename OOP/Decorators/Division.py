# 09.01.2022
# Decorator for division function

def Division(value1,value2):  # 0x100
	Ans = value1 / value2
	return Ans

def SmartDivision(Function_Name):   # def SmartDivision(0x100)
	def inner(x,y):   # 0x200
		if(y == 0):
			print("ZeroDivisionError: Division by zero is undefined ")
			return None      # return none to main
		else:
			return Function_Name(x,y)   # firstly call to Division function then return ans to the main function 
	return inner    # return hash code of inner function to the main 
	
Division = SmartDivision(Division)  
# Division = SmartDivision(0x100)

def main():
	no1 = int(input("Enter First Number : "))
	no2 = int(input("Enter Second Number : "))
	
	Ret = Division(no1,no2)
	print("Division is : ",Ret)

if __name__ == "__main__":
	main()

