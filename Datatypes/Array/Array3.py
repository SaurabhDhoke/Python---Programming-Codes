""" 
Creation of Array in python

Date : 25.12.2021
"""

import array as ARR

def main():
	print("Demonstration of array in python ")
	
	data = ARR.array('i',[10,20,30,40,50])
	print(data)
	print("Length of array : ",len(data))
	print("Type is : ",type(data))
	
	print(data[0])
	print(data[1])
	
	print("------------------------------------------------------")
	
	for i in range(len(data)):
		print(data[i],end ="\t")	
	
	print("\n---------------------------------------------------")
	
	i = 0
	while(i <len(data)):
		print(data[i],end =" ")
		i = i + 1
		
	print("\n--------------------------------------------------")
	
	for no in data:
		print(no,end =" ")
		
	print("\n--------------------------------------------------")



if __name__ == "__main__": 
	main()

