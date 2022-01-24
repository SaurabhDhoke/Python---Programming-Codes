"""
serial programming

Date : 15.01.2022
"""

import os
import multiprocessing

def Fun(X):
	print("inside Fun")
	print("PID of Fun : ",os.getpid())
	for i in range(X):
		print("Fun : ",i)
	
def Gun(X):
	print("inside Gun")
	print("PID of Gun : ",os.getpid())
	for i in range(X):
		print("Gun : ",i)
	
def main():
	print("inside main")
	print("PID of Parent process : ",os.getpid())
	
	Fun(5)
	Gun(10)

if __name__ == "__main__":
	main()























