"""
Automation Script 1
Addition of two numbers
Date : 22.1.2020
"""

# import statements if necessary
from sys import *

"""------------------------------------------------------------------"""

def Addition(iNo1,iNo2):
	Ans = iNo1 + iNo2
	return Ans
	
"""------------------------------------------------------------------"""

# Entry point of automation script
def main():
	print("-----------Shiv_Shambho : Automation3-----------")
	print("Script name : ",argv[0])
	print("Number of arguments accepted : ",len(argv)-1)
		
	if (len(argv)>3) or (len(argv)<2):
		print("Invalid number of arguments...")
		print("Use -u flag for usage ")
		print("Use -h flag for Help")
		exit()
	
	if (len(argv) == 2):
		if (argv[1]=="-u") or (argv[1]=="-U"):
			print("Usage : Script is used to perform the addition of 2 numbers ")
			exit()
		elif (argv[1]=="-h") or (argv[1]=="-H"):
			print("Help : Name_of_Sript First_Argument Second_Argument ")
			print("First_Argument : Any numeric Value")
			print("Second_Argument : Any numeric Value")
			exit()
		else:
			print("There is no such a flag...")
			exit()
			
	if (len(argv) == 3):
		try:
			iRet = Addition(int(argv[1]),int(argv[2]))
			print("Addition is : ",iRet)
		
		except Exception:
			print("Exception while executing the Script")
			print("Check the input or contact the developer")

"""------------------------------------------------------------------"""	

#starter of the automation script
if __name__ == "__main__":
	main()
	
"""------------------------------------------------------------------"""


