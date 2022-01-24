# Date : 18.12.2021
# tuple
# as karu naye 
# Append karata yet nahi tuple madhi but as karu shakato pn karu nye

Data = (10,20,30,40)

print("Original Data : ",Data)

Data = list(Data)
Data.append(50)

Data = tuple(Data)
print("Updated Data : ",Data)
