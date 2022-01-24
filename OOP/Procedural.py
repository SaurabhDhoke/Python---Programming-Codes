
# Date : 01.01.2022

def Addition(a,b):
	return a+b

def main():
	print("Enter first number : ")
	no1 = int(input())

	print("Enter Second number : ")
	no2 = int(input())

	ret = Addition(no1,no2)
	print("Addition is : ",ret)

if __name__ == "__main__":
	main()
