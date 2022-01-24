"""
Date : 09.01.2022
"""

def Division(A,B):
	ans = 0.0
	try:
		ans = A/B     # exception prone code
	
	except ZeroDivisionError as obj:
		print("Exception occured in ZeroDivisionError block")
		print("Exception statement is : ",obj)
		
	except Exception as obj:   # generic except block
		print("Exception Occured in Exception block")
		
		
	return ans

def main():
	no1 = int(input("Enter First Number : "))
	no2 = int(input("Enter Second Number : "))
    
	Ret = Division(no1,no2)
	print("Division is : ",Ret)
	
if __name__ == "__main__":
	main()
