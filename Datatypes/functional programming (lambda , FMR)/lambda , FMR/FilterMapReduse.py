"""
filter map reduse

Accept list from user and list the even numbers and increament by 2 those even numbers and and that numbers print on screen 

Date : 26.12.2021
"""

from functools import reduce    # for reduce function
#--------------------------------------------------		

def CheckEven(no):
	return(no%2 == 0)
"""	
	if(no%2 == 0):
		return True
	else:
		return False
"""
#--------------------------------------------------	
	
def Increament(no):
	return no+2

#--------------------------------------------------		

def Addition(a,b):
	return a+b

#--------------------------------------------------		

def main():
	data = [5,7,6,8,4]
	print("Originnal data : ",data)
	
	#--------- filter(function,list)
	newdata = list(filter(CheckEven,data))
	print("Data after filter : ",newdata)
	
	#--------- map(function,list)
	incrementdata = list(map(Increament,newdata))
	print("Data after map : ",incrementdata)

	#--------- reduce(function,list)
	Ret = reduce(Addition,incrementdata)
	print("Data after reduce : ",Ret)
	
	
	
#--------------------------------------------------			
if __name__ == "__main__":
	main()


