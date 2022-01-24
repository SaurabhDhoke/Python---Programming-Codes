"""
Automation Script 1
Template
Date : 22.1.2020
"""

# import statements if necessary
from sys import *

# Entry point of automation script
def main():
	print("-----------Shiv_Shambho : Automation1-----------")
	print("Script name : ",argv[0])
	print("Number of arguments accepted : ",len(argv)-1)
	
	if (len(argv)>3) or (len(argv)<2):
		print("Invalid number of arguments...")
		exit()
	
	if (argv[1]=="-u") or (argv[1]=="-U"):
		print("Usage : Script is used to perform the addition of 2 numbers ")
		exit()
	
	if (argv[1]=="-h") or (argv[1]=="-H"):
		print("Help : Name_of_Sript First_Argument Second_Argument ")
		print("First_Argument : Any numeric Value")
		print("Second_Argument : Any numeric Value")
		exit()
	
#starter of the automation script
if __name__ == "__main__":
	main()

