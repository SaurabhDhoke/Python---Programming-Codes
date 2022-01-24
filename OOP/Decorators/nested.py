# Date : 08.01.2022
# nested Functions

def outer():
	print("Inside outer function")
	
	def Inner():
		print("Inside Inner Function")
	
	Inner()
	
def main():
	outer()

if __name__ == "__main__":
	main()










