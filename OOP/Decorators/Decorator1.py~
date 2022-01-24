# Date : 08.01.2022
# Decorator

def Division(x,y):    # 0x100
	Ans = 0.0
	Ans = x/y
	return Ans

def SmartDivision(Func_Name): # Func_Name = 0x100
	def Inner(a,b):    # 0x200
		if(a < b):
			a,b = b,a  # multi variable Assignment
			
		return Func_Name(a,b)  # return 0x100(a,b)  Division la call gela
	return Inner # return 0x200

# he adhi run honar nantr if nd nantr main run hoil	
Division = SmartDivision(Division)	# Division = SmartDivision(0x100)
									# Division = 0x200
def main():	
	No1 = 0
	No2 = 0
	
	No1 = int(input("Enter first Number : "))
	No2 = int(input("Enter Second Number : "))
	
	ret = Division(No1,No2)  # 0x200(5,10)
	print("Division is : ",ret)
	
	
#---------------------------------------------------	
if __name__ == "__main__":
	main()
#---------------------------------------------------	


