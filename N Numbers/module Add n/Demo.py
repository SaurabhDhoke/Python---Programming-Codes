
# Accept n numbers from user and Display Addition (by module)
# Date : 18.12.2021

import Marvellous

def main():
	size = 0
	i = 0
	Data = []	
	
	print("How many Elements you want : ")
	size = int(input())

	print("Enter the elements : ")
	for i in range(size):
		Data.append(int(input()))
		
	print("Your Entered Data is ",Data)
	
	Ret = Marvellous.Addition(Data)
	print("Addition is : ",Ret)

if __name__ == "__main__":
	main()

