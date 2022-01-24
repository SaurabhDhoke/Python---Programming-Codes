"""
 global variable 
 Date : 08.01.2022
"""
i = 0            # defination of i
def fun():
	global i     # declaration of i
	if (i < 5):
		print(i)
		i = i+1   # i++
		fun()     # Recursive call

def main():
	fun()

	
if __name__ == "__main__":
	main()

