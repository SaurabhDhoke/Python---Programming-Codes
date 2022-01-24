"""
 Creation User defined filter map reduce functions
 Date : 30.12.2021
"""


from FMR import *

#--------------------------------------------------		

CheckEven = lambda no : (no%2 == 0)
Increament = lambda no : no+2
Addition = lambda a,b : a+b

#--------------------------------------------------		

def main():
	data = [5,7,6,8,4]
	print("Originnal data : ",data)
	
	newdata = list(filterX(CheckEven,data))
	print("Data after filter : ",newdata)

	incrementdata = list(mapX(Increament,newdata))
	print("Data after map : ",incrementdata)

	Ret = reduceX(Addition,incrementdata)
	print("Data after reduce : ",Ret)
	
#--------------------------------------------------			
if __name__ == "__main__":
	main()


