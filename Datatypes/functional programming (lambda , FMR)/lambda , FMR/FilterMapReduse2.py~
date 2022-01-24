"""
filter map reduse  by using lambda
as karu naye

Accept list from user and list the even numbers and increament by 2 those even numbers and and that numbers print on screen 

Date : 26.12.2021
"""

from functools import reduce    # for reduce function

def main():
	data = [5,7,6,8,4]
	print("Originnal data : ",data)
	
	newdata = list(filter(lambda no : (no%2 == 0),data))
	print("Data after filter : ",newdata)
	
	incrementdata = list(map(lambda no : no+2,newdata))
	print("Data after map : ",incrementdata)

	Ret = reduce(lambda a,b : a+b,incrementdata)
	print("Data after reduce : ",Ret)
	
	
if __name__ == "__main__":
	main()


