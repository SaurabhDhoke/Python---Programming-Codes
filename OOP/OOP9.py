"""
Single level Inheritance

Date : 02.01.2022
"""

#------------------------------------------------------
class Base:
	def __init__(self):
		print("Inside base Constructor")
		self.A = 10
		
	def fun(self):
		print("Base fun")
	
#------------------------------------------------------
class Derived(Base):
	def __init__(self):
	#	Base.__init__(self)
		super().__init__()     # both are same
		
		print("Inside derived constructor")
		self.B = 20


	def gun(self):
		print("Derived gun")
#------------------------------------------------------

def main():
	dobj = Derived()
	dobj.fun()
	print(dobj.A)
	
	
#------------------------------------------------------
if __name__ == "__main__":
	main()
#------------------------------------------------------


"""
class derived : public base    c++
class derived extends base     java
"""
