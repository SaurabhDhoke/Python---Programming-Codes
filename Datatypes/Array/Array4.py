""" 
Creation of Array in python

Date : 25.12.2021
"""

import array as ARR

def main():
	print("Demonstration of array in python ")
	
	data = ARR.array('f',[10.1,20.2,30.3,40.4])
	print(data)
	print("Length of array : ",len(data))
	print("Type is : ",type(data))
	
	print(data[0])
	print(data[1])
	
	print("------------------------------------------------------")
	
	for i in range(len(data)):
		print(data[i],end ="\t")	
	
	print("\n--------------------------------------------------")
    
	print("type code of array is : ",data.typecode)




if __name__ == "__main__": 
	main()

