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

exampleModule.exampleFunc('test')


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