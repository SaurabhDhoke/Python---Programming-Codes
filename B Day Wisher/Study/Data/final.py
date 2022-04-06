"""---------------------------------------------------------------------
Programmer Name : Dhoke Saurabh Vilas 
Script Usage    : final
Date            : 14.03.2022
---------------------------------------------------------------------"""

import time
from datetime import date
import pandas as pd

import os
import psutil
import time

from sys import *
import schedule

from urllib.request import urlopen
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

"""----------------------------------------------------------------"""
def is_connected():
	try:
		urlopen('https://www.google.com/')
		return True
	except:
		return False

"""----------------------------------------------------------------"""
def Mail(bday_boy_mid,BODY):	
	connected = is_connected()
	
	if connected :
		MailSender(bday_boy_mid,BODY)
	else:
		print("There is no internet Connection...connect Wifi to PC and then Run the script")	
	
	print()	

"""----------------------------------------------------------------"""
def MailSender(bday_boy_mid,BODY):
	try:
		from_address = "thisissaurabhdhoke@gmail.com"
		to_address = bday_boy_mid
		
		msg = MIMEMultipart()
		msg['From'] = from_address
		msg['To'] = to_address

		body = BODY
		
		Subject = """B-Day Wishes"""
		
		msg['Subject'] = Subject
		msg.attach(MIMEText(body,'plain'))
		
		s = smtplib.SMTP('smtp.gmail.com',587)
		s.starttls()
		s.login(from_address,"30883088")
		
		text = msg.as_string()
		s.sendmail(from_address,to_address,text)
		s.quit()
		print("Mail successfully sent")

	except Exception as E:
		print("Unable to send mail",E)

"""----------------------------------------------------------------"""
def Compare_dates():
	t = time.localtime()
	current_date = time.strftime("%d/%m",t) 

	File = pd.read_csv('Bday_information.csv')

	list_name    = File.Name
	list_mail_id = File.Mail_id
	list_b_date  = File.B_Date
	list_programmer = File.Programmer

	bday_boy_mid = 0
	it_non_it = "Yes"

	for i in range(0,len(list_b_date),1):
		if current_date == list_b_date[i]:
			bday_boy_mid = list_mail_id[i]
			it_non_it = list_programmer[i]
			
			if it_non_it == "Yes":
				fd = open("Bday_wish_programmer.txt",'r')
				BODY = fd.read()
				fd.close()
				Mail(bday_boy_mid,BODY)
				
			else:
				fd = open("Bday_wish.txt",'r')	
				BODY = fd.read()
				fd.close()
				Mail(bday_boy_mid,BODY)
				
"""----------------------------------------------------------------"""			
			
def main():
	print("\n-------------- Shiv Shambho : Bday Wisher Script ------------------")
	print("Application Name : "+argv[0])
	
	if (len(argv) == 2):
		if ((argv[1] == "-h") or (argv[1] == "-H")):	
			print("This script is used to wish to freind on her bday automatically and write name of friend into log file")
			exit()
			
		if ((argv[1] == "-u") or (argv[1] == "-U")):	
			print("Usage : Application_Name")
			exit()


	while(1):
		try:
			startTime = time.time()
			Compare_dates()
			endTime = time.time()		
			print('Took %s seconds to Run this script.' %(endTime - startTime))
			time.sleep(86400)
		
		except ValueError:
			print("Error : Invalid datatype of input")
		except Exception as E:
			print("Error : Invalid input",E)
			
		
"""----------------------------------------------------------------"""
if __name__ == "__main__":
	main()
"""----------------------------------------------------------------"""			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
