"""
Shedualar script
it prints date and time after 1 minutes

Date : 22.1.2020
"""

"""------------------------------------------------------------------"""
import time			# inbuild module
import datetime		# inbuild module
import schedule     # pip install shedule
"""------------------------------------------------------------------"""
def task():
	print("Task after each minute gets executed")
	print("Current time is : ",datetime.datetime.now())
"""------------------------------------------------------------------"""

def main():
	print("Inside main function")
	print("Scheular starts...")
	
	schedule.every(1).minutes.do(task)  # function ch nav pathavayach only call nay karayach function
	
	while True:
		schedule.run_pending()
		time.sleep(1)

"""------------------------------------------------------------------"""

if __name__ == "__main__":
	main()
	
"""------------------------------------------------------------------"""


