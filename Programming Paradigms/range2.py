# Date : 18.12.2021
# Accept value from user and print hello on screen that no of times

def Iteration(value):
	for i in range(value):
		print("Hello")

def main():
	print("Enter the freuency : ")
	no = int(input())
	Iteration(no)
	
if __name__ == "__main__":
	main()
