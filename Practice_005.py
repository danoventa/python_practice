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

gradeDict = {'Kelly':90, 'David':65, 'Jack':95, 'Samantha':95}

print (gradeDict)
print(gradeDict['David'])
gradeDict['David'] = 45
print(gradeDict['David'])

gradeDict['Jessey'] = 92
del gradeDict['David']
print (gradeDict)

gradeDict = {'Kelly':[90, 95], 'Jack':[95, 99], 'Samantha':[95, 94], 'Jessey':[92, 93]}
print(gradeDict['Jessey'])
print(gradeDict['Jessey'][0])

# mutable can be changed (list)  - []
# immutable cannot be changed (tuple)   - ()

x = [2, 3, 5, 2, 5, 6, 7]
print (x)
print (x[4])
x.append(12)
print (x)
x.insert(5, 7)
print (x)
x.remove(7)
print(x)
print((x.index(2)))
print(x.count(3))
x.sort()
print(x)

def example():
	return 15, 19
	
a, b = example()

print (a)
print (b)


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