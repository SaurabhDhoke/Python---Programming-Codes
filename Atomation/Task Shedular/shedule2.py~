"""
Shedualar script

consider the python application which schedule task after minutes ,hour,as well as on specific Day or specific time.

Date : 24.1.2020
"""

"""------------------------------------------------------------------"""
import time			# inbuild module
import datetime		# inbuild module
import schedule     # pip install shedule
"""------------------------------------------------------------------"""

def fun_Minute():
	print("Current time is : ")
	print(datetime.datetime.now())
	print("Schedular executed after Minute")

"""------------------------------------------------------------------"""

def fun_Hour():
	print("Current time is : ")
	print(datetime.datetime.now())
	print("Schedular executed after Hour")
	
"""------------------------------------------------------------------"""

def fun_Day():
	print("Current time is : ")
	print(datetime.datetime.now())
	print("Schedular executed after Day")

"""------------------------------------------------------------------"""

def fun_Afternoon():
	print("Current time is : ")
	print(datetime.datetime.now())
	print("Schedular executed at 12")

"""------------------------------------------------------------------"""
def main():
	print("------------- Shiv Shambho : Python Automation -------------")
	print("python Job shedular")
	print(datetime.datetime.now())
	
	schedule.every(1).minutes.do(fun_Minute)
	schedule.every().hour.do(fun_Hour)
	schedule.every().day.at("00:00").do(fun_Afternoon)
	schedule.every().sunday.do(fun_Day)
	schedule.every().saturday.at("18:30").do(fun_Day)
	
	while True:
		schedule.run_pending()
		time.sleep(1)
		
"""------------------------------------------------------------------"""

if __name__ == "__main__":
	main()
	
"""------------------------------------------------------------------"""


