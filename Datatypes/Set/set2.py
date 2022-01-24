# Date : 25.12.2021
# Accept elements from user and store it into set

print("Enter number of elements :")
size = int(input())

data = set()   # set navachya class cha constructor call kela

for i in range(size):
	print("Enter Element no : ",i+1)
	no = int(input())
	data.add(no)

print("Data from set is : ",data)

print("Enter data to search : ")
value = int(input())

if value in data:
	print("Element is there")
else:
	print("There is no such element")

