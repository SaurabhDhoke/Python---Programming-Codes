# Date : 18.12.2021
# display elements of list by loop

# List
# sequential
# indexed
# data is mutable
# list is mutable
# allows duplicate
# Heterogenious



Data = [11,21,51,101,111]


print("Data using while loop")
i = 0

while(i < len(Data)):
	print(Data[i])
	i = i+1


print("Data using for loop")

# for i in range(5)
# for i in range(0,5,1)

for i in range(len(Data)):
	print(Data[i])






