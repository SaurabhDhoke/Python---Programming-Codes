"""
Addition of two numbers by Command line arguments

Date : 22.1.2020
"""

from sys import *

def main():
	print("Data type of command line argument : ",type(argv[1])) # class str
	ans = int(argv[1]) + int(argv[2])
	print("Addition is : ",ans)
	
	
if __name__ == "__main__":
	main() 


