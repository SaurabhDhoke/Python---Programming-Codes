""" user defined FMR module"""

"""--------------------------------------------------	
		This is a userdefind filter function
--------------------------------------------------"""
def filterX(fun_name,data):
	filtered_list = []
	for no in data:
		Ret = fun_name(no)
		if(Ret == True):
			filtered_list.append(no)		
	return filtered_list





"""--------------------------------------------------	
		This is a userdefind map function
--------------------------------------------------"""
def mapX(fun_name,data):
	mapped_list = []
	for no in data:
		Ret = fun_name(no)
		mapped_list.append(Ret)
	return mapped_list
	
	
	
	
"""--------------------------------------------------	
		This is a userdefind reduce function
--------------------------------------------------"""
def reduceX(fun_name,data):
	Result = 0
	for no in data:
		Result = fun_name(Result,no)
	return Result


