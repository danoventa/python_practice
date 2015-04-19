print('Hello World')
print(4**2)

exVar = 100
print(exVar)
opVar = exVar / 5.3
print(opVar)

condition = 1
while condition < 10:
	print(condition)
	
	#condition = condition + 1
	'''
		multiple lines
		can go here
	'''
	
	condition += 1
	
condition = 5
while condition < 15:
	print('true')	
	condition += 1	
	
exampleList = [1, 6, 3, 4, 6, 14, 4, 90]	
for thing in exampleList:
	print(thing)

for x in range(1, 11):
	print(x)
	
x = 2
y = 7
z = 10

if x > y:
	print(x, 'is greater than', y)
if x < y:
	print(x, 'is less than', y)
if x==y:
	print(x, 'is equal to', y)
	
if x <= y: 
	print(x, 'is less than or equal to', y)

if z > y > x:
	print(z, 'is greater than', y, 'which is greater than', x)

x = 3
y = 6

if x < y:
	print(x, 'is less than', y)
if x > y:
	print(x, 'is greater than', y)
else:
	print(x, 'is not greater than', y)
	
if x > y:
	print('x is greater than y')
elif x < z:
	print(x,'is less than', z)
else:
	print('nothing was the case')
	

