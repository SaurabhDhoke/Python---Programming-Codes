# Date : 08.01.2022
# Recursion

def DisplayR(no):
	if(no > 0): 
		print("Marvellous")
		no = no - 1
		DisplayR(no)  # Recursive call
	
def main():
	DisplayR(10)

if __name__ == "__main__":
	main()




