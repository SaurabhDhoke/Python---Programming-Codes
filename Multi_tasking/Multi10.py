"""
parrallal programming

Date : 15.01.2022
"""
import os
import multiprocessing

def Square(No):
	print("PID is : ",os.getpid())
	return No*No


def main(): 
	data = [5,3,1,4,8,2]
	
	p = multiprocessing.Pool()
	
	result = list()
	
	result = p.map(Square,data)
	
	print("Result is : ",result)


if __name__ == "__main__":
	main()























