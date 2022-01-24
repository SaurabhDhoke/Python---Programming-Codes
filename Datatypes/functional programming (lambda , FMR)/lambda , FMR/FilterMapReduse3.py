"""
filter map reduse  by using lambda
as karu naye

Accept list from user and list the even numbers and increament by 2 those even numbers and and that numbers print on screen 

Date : 26.12.2021
"""

from functools import reduce    # for reduce function


def main():
	
	print("Data after reduce : ",reduce(lambda a,b : a+b,list(map(lambda no : no+2,list(filter(lambda no : (no%2 == 0),[5,7,6,8,4]))))))
	
	
if __name__ == "__main__":
	main()


