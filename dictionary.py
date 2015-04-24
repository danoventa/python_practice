from __future__ import print_function
import sys
import os 

DIR = "./tmp/collat_test/"

def parse_file():
	os.chdir(DIR)
	for root, dirs, files in os.walk("."):
		for file in files:
			if file.endswith(".txt"):
				f = open(file, 'r')
        		content = f.readlines()
        		print(content)
        		parse_words(content)

def parse_words(readFile):
	primatives = [];
	undefinedWords = [];
	line = ""
	for lines in readFile.readlines():
		print(lines)		
		for word in lines.split(' '):
			yield word
			print(word)
		
def main(): 
	parse_file()
	pass     		

if __name__ == '__main__':
	sys.exit(main())
