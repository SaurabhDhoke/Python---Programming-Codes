# Date : 08.01.2022
# Decorator

def Division(a,b):
	Ans = 0.0
	Ans = a/b
	return Ans


def main():	
	No1 = 0
	No2 = 0
	
	No1 = int(input("Enter first Number : "))
	No2 = int(input("Enter Second Number : "))
	
	ret = Division(No1,No2)
	print("Division is : ",ret)
	
	
#---------------------------------------------	

if __name__ == "__main__":
	main()










