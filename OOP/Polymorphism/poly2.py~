"""
polymorphisom (method overriding)

Date : 09.01.2022
"""
#---------------------------------------------------
class Base:
	def __init__(self):
		self.i = 10
		self.j = 20

	def fun(self):
		print("Base Fun")	
	
	def gun(self):
		print("Base gun")
		
#---------------------------------------------------		
class Derived(Base):
	def __init__(self):
		self.a = 11
		self.b = 21
	
	def fun(self):
		print("Derived Fun")

	def sun(self):
		print("Derived sun")
		
#---------------------------------------------------
def main():
	bobj = Base()
	dobj = Derived()
	
	bobj.fun()     # Base Fun
	dobj.fun()     # Derived Fun
	dobj.sun()     # Derived sun
	dobj.gun()     # Base gun
	

#---------------------------------------------------
if __name__ == "__main__":
	main()

















