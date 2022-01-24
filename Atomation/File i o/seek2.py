"""
seek file 
    0 for begining
	1 for current
    2 for end
	
Date : 22.1.2020
"""

import os 

def main():
	print("Enter the file name that you want to open : ")
	name = input()
	
	fd = open(name,"rb")   # rb = open file in a binary mode
	
	data = fd.read(5)
	fd.seek(-4,2)  
	
	data = fd.read()
	print(data)
	
if __name__ == "__main__":
	main()

# Helloworld

