
# Accept two numbers from user and perform Addition by function
# Date : 5.12.2021

def Addition(value1 ,value2):
	ans = value1 + value2;
	return ans;

def main():
	print("Marvellous Addition Application")
	no1 = int(input("Enter first number : "))
	no2 = int(input("Enter second number : "))
	
	ret = Addition(no1,no2);
	print("Addition is : ",ret);
		
if __name__=="__main__":
	main();























