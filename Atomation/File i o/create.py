"""
create file 
by using open call you can also create file

Date : 22.1.2020
"""

def main():
	print("Enter the file name that you want to create : ")
	name = input()
	
	fd = open(name,"x")  
	print("File gets created with the information as : ",fd)
	
if __name__ == "__main__":
	main()

