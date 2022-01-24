"""
process based Parallal programming
(heavy)
Date : 15.01.2022
"""

import os
import multiprocessing
#---------------------------------------------
def Fun(X):
	print("inside Fun")
	print("PID of Fun : ",os.getpid())
	print("PPID of Fun : ",os.getppid())
	
	for i in range(X):
		print("Fun : ",i)
#----------------------------------------------	
def Gun(X):
	print("inside Gun")
	print("PID of Gun : ",os.getpid())
	print("PPID of Gun : ",os.getppid())
	
	for i in range(X):
		print("Gun : ",i)
#---------------------------------------------
def main():
	No = 5
	print("inside main")
	print("PID of Parent process : ",os.getpid())
	
	process1 = multiprocessing.Process(target = Fun, args = (No,))
	process2 = multiprocessing.Process(target = Gun, args = (No,))
	
	process1.start()  # to run process1
	process2.start()  # to run process2
	
	process1.join()   # child process ch execution complete hot nay tover main la thambun thevl ya line na
	process2.join()
	
	print("End of main")
#---------------------------------------------
if __name__ == "__main__":
	main()























