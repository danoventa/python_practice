from __future__ import print_function
import sys
import os 

DIR = "./tmp/collat_test/"

def to_defined(toBeDefined):
	print(toBeDefined)
	
def already_defined(defined):
	print(defined)

def parse_file():
	os.chdir(DIR)
	for root, dirs, files in os.walk("."):
		for file in files:
			if file.endswith(".txt"):
				toBeDefined = [];
				defined = [];
				fi = open(file, 'r').read()
				content2 = fi.split('\n')
				print(content2)
				for line in content2:
					print(line)
					if "." in line:
						line.split(" ")
						defined.append(line[0])
						already_defined(defined)
						print('is definition')
					else:
						toBeDefined.append(line)
						to_defined(toBeDefined)
						print('undefined')
				print ("finished the line loop")

		
def main(): 
	parse_file()
	pass     		

if __name__ == '__main__':
	sys.exit(main())
