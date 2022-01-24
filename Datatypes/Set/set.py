# Date : 25.12.2021
# set


data ={10,20,30,40}
mylist= [10,20,30,40]

print("Datatype is : ",type(data))
print("length is : ",len(data))

print("Data from set : ",data)   # 40 10 20 30
print("Data from list : ",mylist)   # 10 20 30 40

# print(data[0])   # cant access by index

print("Data traversal using loop")
for no in data:
	print(no,end = " ")


data1 = {10,20,30,40,10}     # duplicate elements are allowed but stored only once 
print("\nNew set is : ",data1)

data2 = {10,20,30.5,"Hello",True}
print(data2)

