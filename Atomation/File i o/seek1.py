"""
seek file

Date : 22.1.2020
"""

import os 

def main():
	print("Enter the file name that you want to open : ")
	name = input()
	
	fd = open(name,"rb")   # rb = open file in a binary mode
	print("Current offset is : ",fd.tell())   # 0
	
	data = fd.read(2)
	print("Data is : ",data)
	print("Current offset is : ",fd.tell())   # 2
	
	# 0 for begining
	# 1 for current
	# 2 for end
	
	fd.seek(5,1)  
	print("Current offset is : ",fd.tell())   # 3
	
	data = fd.read()
	print(data)
	
if __name__ == "__main__":
	main()

# Helloworld

