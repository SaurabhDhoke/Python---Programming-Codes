"""
read file 

Date : 22.1.2020
"""

import os 

def main():
	print("Enter the file name that you want to open : ")
	name = input()
	
	if os.path.exists(name):
		fd = open(name,"r")  
		print(type(fd))
		
		# data = fd.read()  # to read whole file
		data = fd.read(5) # to read first 5 bytes
		
		print("Data from file is : ",data)
		fd.close()
	
	else:
		print("There is no such a file")
	
if __name__ == "__main__":
	main()

