"""---------------------------------------------------------------------
Programmer Name : Dhoke Saurabh Vilas 
Script Usage    : read data from csv
Date            : 13.03.2022
---------------------------------------------------------------------"""


import pandas as pd

File = pd.read_csv('Bday_information.csv')

print(File)
print("-"*100)

print(File.head())
print("-"*100)

List = File.Mail_id

print(List[1])
print("-"*100)









