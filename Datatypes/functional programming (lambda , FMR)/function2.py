"""
keyword arguments

Date : 26.12.2021
"""

def Addition(No1,No2):            # function defination
	Ans = 0
	Ans = No1 + No2
	return Ans	

def main():
	print("Enter First Number : ")
	value1 = int(input())
	print("Enter second Number : ")
	value2 = int(input())
	
	# keyword arguments
	Ret = Addition(No1 = value1,No2 = value2)   # function call
	print("Addition is ",Ret)
	
	
if __name__ == "__main__":
	main()


