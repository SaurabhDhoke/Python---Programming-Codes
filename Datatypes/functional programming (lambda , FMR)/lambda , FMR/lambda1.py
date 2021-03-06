"""
functional programming 

Date : 26.12.2021
"""

# named function
def Add(a,b):                # procedural approach
	return a+b   

# lambda/Anonimus  function
Addx = lambda a,b : a+b      # functional approach


def main():
	Ret = Add(10,20)
	print("Addition is : ",Ret)
	
	Ret = Addx(10,20)
	# Ret = 10+20
	print("Addition is : ",Ret)
	
	print(type(Add))				 # <class 'function'>
	print(type(Addx))   			 # <class 'function'>
	print(type(lambda a,b : a+b))    # <class 'function'>
	print(lambda a,b : a+b)          # <lambda> at 0x7f586de27160>

	
	
if __name__ == "__main__":
	main()


