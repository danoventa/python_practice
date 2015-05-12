from __future__ import print_function
import sys
import os 

DIR = "./tmp/collat_test/"


'''		if  len(temp.split(" ")) > 1:   '''
def find_definition(undefined, defined):
	while undefined:
		temp = undefined.pop()
		if len(temp.split(" ")) > 1:
			tempList = temp.split(" ")
			for word in tempList:
				if any(word in s for s in defined):
					print("THIS IS LIST")
					print (tempList)
					print(temp)
					print ("Has Been Defined: " + temp )
					defined.append(temp)
		print(defined)
	definedString = ''
	for word in defined:
		print(word)
		
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

if __name__ == '__main__':
	sys.exit(main())
