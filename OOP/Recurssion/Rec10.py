"""

 Date : 08.01.2022
"""

def fun():
	# static int i = 0    in c/c++ ( no static variable in python and java)
	i = 0         # local variable (auto storage class)
	if (i < 5):
		print(i)
		i = i+1   # i++
		fun()     # Recursive call

def main():
	fun()

	
if __name__ == "__main__":
	main()

