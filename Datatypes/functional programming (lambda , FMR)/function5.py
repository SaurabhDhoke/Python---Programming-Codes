"""
Arbitary arguments
Accept multiple numbers and print there addition on screen

Date : 26.12.2021
"""

def Addition(*value):
	sum = 0
	for no in value:
		sum = sum + no
		
	return sum
	
	
def main():
	Ret = Addition(10,20,30,40,50)    # 150
	print("Addition is : ",Ret)
	
	Ret = Addition(10,20,30,40)       # 100
	print("Addition is : ",Ret)
	
	Ret = Addition()
	print("Addition is : ",Ret)       # 0
	
	
if __name__ == "__main__":
	main()


