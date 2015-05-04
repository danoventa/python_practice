from __future__ import print_function
import sys
import os 

DIR = "./tmp/collat_test/"

def find_definition(undefined, defined):
	while undefined:
		temp = undefined.pop()
		if  len(temp.split(" ")) > 1:
			if temp.split(" ")[1] in defined:
				defined.append(temp.split(" ")[0])
		print ("Has Been Defined: " + temp)
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
						defined.append(line.split(" ")[0])
						print('is definition')
					else:
						toBeDefined.append(line)
						print('undefined')
				print ("finished the line loop")
				find_definition(toBeDefined, defined)

def main(): 
	parse_file()
	pass     		

if __name__ == '__main__':
	sys.exit(main())
