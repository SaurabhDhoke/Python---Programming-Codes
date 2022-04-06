"""---------------------------------------------------------------------
Programmer Name : Dhoke Saurabh Vilas 
Script Usage    : compare dates and make another list of bday boys
Date            : 13.03.2022
---------------------------------------------------------------------"""

import time
from datetime import date
import pandas as pd

t = time.localtime()
current_date = time.strftime("%d/%m",t) 

File = pd.read_csv('Bday_information.csv')

list_name    = File.Name
list_mail_id = File.Mail_id
list_b_date  = File.B_Date

"""
for i in range(0,len(list_b_date),1):
	if current_date == list_b_date[i]:
		print("Mail_id : ",list_mail_id[i])
		print("Name : ",list_name[i])
		print("Happy Bday : ",list_name[i])
"""

bday_boys = []

for i in range(0,len(list_b_date),1):
	if current_date == list_b_date[i]:
		bday_boys.append(list_mail_id[i])

print("Bday Boys : ",bday_boys)
