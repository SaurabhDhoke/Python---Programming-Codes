# Date : 08.01.2022
# function pass to another Function

# 0x100
def fun():
	print("Inside fun")

# 0x200
#def gun(0x100):
def gun(Func_Name): # fun cha hash code pakadala Func_Name madhi
	print("Inside gun")
	Func_Name()  #  internalli as zal fun()   0x100()
	
def main():
	gun(fun)  #gun(0x100)
	
if __name__ == "__main__":
	main()










