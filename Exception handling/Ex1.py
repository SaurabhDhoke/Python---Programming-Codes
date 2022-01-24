"""
 problematic code
 ZeroDivisionError: division by zero
 exception prone code : ans = A/B

Date : 09.01.2022
"""

def Division(A,B):
	ans = 0.0
	ans = A/B     # exception prone code
	return ans

def main():
	no1 = int(input("Enter First Number : "))
	no2 = int(input("Enter Second Number : "))
    
	Ret = Division(no1,no2)
	print("Division is : ",Ret)
	
if __name__ == "__main__":
	main()
