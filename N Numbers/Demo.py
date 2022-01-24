
# Accept n numbers from user and Display on Screen
# Date : 18.12.2021

def main():
	size = 0
	i = 0
	no = 0
	
	print("How many Elements you want : ")
	size = int(input())
	
	Data = []
	
	print("Enter the elements : ")
	for i in range(size):
		no = int(input())
		Data.append(no)
		
	print("Your Entered Data is ",Data)
	
if __name__ == "__main__":
	main()

