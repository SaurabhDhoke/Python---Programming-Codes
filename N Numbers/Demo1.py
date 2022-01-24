
# Accept n numbers from user and Display Addition
# Date : 18.12.2021

def Addition(value):
	sum = 0
	for i in range(len(value)):
		sum = sum+value[i]
	
	return sum


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
	
	Ret = Addition(Data)
	print("Addition is : ",Ret)

if __name__ == "__main__":
	main()

