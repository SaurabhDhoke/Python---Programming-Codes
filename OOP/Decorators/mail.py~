# Date : 08.01.2022


def sub(a,b):
	print(a-b)

def SmartSub(fptr):
	def inner(a,b):
		if a<b:
			a,b = b,a
		return fptr(a,b)
	return inner

sub = SmartSub(sub)

print("Substraction of 7 & 2 is : ")
sub(7,2)

print("Substraction of 2 & 7 is : ")
sub(2,7)









