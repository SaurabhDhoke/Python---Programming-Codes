""" 
 creation of Dictonary in python
 Date : 18.12.2021
"""

def main():
	data = {"A" : 10, "B" : 20,"C" : 30,"D" : 40,51:"D"}
	print("Data is   : ",data)
	print("Type is   : ",type(data))
	print("Length is : ",len(data))
	
	# print(data[0])     we cannot access with index
	
	print(data["A"])   # 10
	
	print()
	for keys in data:
		print(keys)          # A B C D
	
	print()
	for keys in data:
		print(data[keys])    # 10 20 30 40
	
	print()
	for keys in data:
		print(keys, data[keys])    # A 10  B 20  C 30  D 50
		 	
		
if __name__ == "__main__":
	main()
