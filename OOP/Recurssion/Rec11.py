"""
UnboundLocalError: local variable 'i' referenced before assignment

 Date : 08.01.2022
"""
i = 0  
def fun():
	if (i < 5):
		print(i)
		i = i+1   # i++
		fun()     # Recursive call

def main():
	fun()

	
if __name__ == "__main__":
	main()

