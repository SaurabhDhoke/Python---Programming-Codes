""" 
 Date : 18.12.2021
"""

def main():
	#      [ py  ,PPA  ,LSP  ,Angular]
	fees = [12500,15000,21000,15500]
	print(fees)
	
	print("Please enter bach name : ")
	batch = input()
	print("Thank you for selecting : ",batch)
	
	if batch == "PPA":
		print("Fees are : ",fees[1])
	elif batch == "LSP":
		print("Fees are : ",fees[2])
	elif batch == "Angular":
		print("Fees are : ",fees[3])
	elif batch == "Python":
		print("Fees are : ",fees[0])
	else :
		print("There is no such a batch in Marvellous..")
	
	
if __name__ == "__main__":
	main()
