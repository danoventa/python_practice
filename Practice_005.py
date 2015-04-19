#input from user:

# the asterix allows you to import everything. 
#from statistics import *

# This allows you to import specifics as a specific name
# from statistics import mean as m, stdev as s

# This will allow you to just use the mean. 
# from statistics import mean
import statistics as s
import exampleModule
exList = [2, 2, 4, 5, 6, 2, 4, 6, 7, 3]

# mutable can be changed (list)
# immutable cannot be changed (tuple)

def example():
	return 15, 19
	
a, b = example()

print (a)
print(b)


exampleModule.exampleFunc('yay it worked!')

# try and except exceptions can be stacked. 
try:
	name = input('what is your name?')
	#print('Running the try...')
	print(str(name))

except TypeError as t:
	print(str(t))

except NameError as n:
	print(str(n))
	
except Exception as e:
	print(str(e))

# Statistics, and input
x = s.mean(exList)
print(x)

x = s.median(exList)
print(x)

x = s.mode(exList)
print(x)

x = s.stdev(exList)
print(x)

name = input('What is your name?: ')
print('Hello', name)