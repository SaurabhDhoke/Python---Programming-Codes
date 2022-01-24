""" 
 creation of Dictonary in python
 Date : 18.12.2021
"""

def main():
	"""	   [ py  ,PPA  ,LSP  ,Angular]
	fees = [12500,15000,21000,15500]
	"""
	#        key       value
	fees = {"Python" : 12500, "PPA" : 15000, "LSP" : 21000, "Angular" : 15500}
	print(fees)
	
	print("Please enter bach name : ")
	batch = input()
	
	print("Thank you for selecting : ",batch)
	print("Fees are : ",fees[batch])
		
	
if __name__ == "__main__":
	main()
