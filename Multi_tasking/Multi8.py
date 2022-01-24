"""
to check count of cpu cores

Date : 15.01.2022
"""

import multiprocessing

def main(): 
	print("Number of cores : ",multiprocessing.cpu_count())

if __name__ == "__main__":
	main()























