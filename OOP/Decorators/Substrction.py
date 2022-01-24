# Substraction by using decorator
# 09.01.2022

def Substraction(value1,value2):   # 0x100
	ans = value1 - value2
	return ans

def SmartSubstraction(Function_Name): # Function_Name = 0x100
	def inner(x,y):   # 0x200
		if(x < y):
			x,y = y,x
		return Function_Name(x,y)
	return inner	

Substraction = SmartSubstraction(Substraction)
# Substraction = SmartSubstraction(0x100)

def main():
	no1 = int(input("Enter First Number : "))
	no2 = int(input("Enter Second Number : "))
	
  # Ret = 0x200(no1,no2)	
	Ret = Substraction(no1,no2) 
	print("Substraction is : ",Ret) 


if __name__ == "__main__":
	main()










