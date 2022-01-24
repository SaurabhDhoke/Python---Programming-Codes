"""
tread based Parallal programming
(light weight)

Date : 15.01.2022
"""

import os
import threading
#---------------------------------------------
def Fun(X):
	print("inside Fun")
	print("PID of Fun : ",os.getpid())   #1000
	print("PPID of Fun : ",os.getppid()) #16203
	
	for i in range(X):
		print("Fun : ",i)
#----------------------------------------------	
def Gun(X):
	print("inside Gun")
	print("PID of Gun : ",os.getpid())   #1000
	print("PPID of Gun : ",os.getppid()) #16203
	
	for i in range(X):
		print("Gun : ",i)
#---------------------------------------------
def main():  #1000
	No = 5
	print("inside main")
	print("PID of Parent process : ",os.getpid())
	
	thread1 = threading.Thread(target = Fun, args = (No,))
	thread2 = threading.Thread(target = Gun, args = (No,))
	
	thread1.start()  # to run thread1
	thread2.start()  # to run thread2
	
	thread1.join()   
	thread2.join()
	
	print("End of main")
#---------------------------------------------
if __name__ == "__main__":
	main()























