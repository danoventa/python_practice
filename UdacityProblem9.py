x = 3.54159
y = 13.5004
z = 3.6200
print(int(str(x)[str(x).find('.') + 1]))
if (int(str(x)[str(x).find('.') + 1]) >= 5):
	print(int(str(x)[:str(x).find('.')]) + 1)
	
test = str(x).find('.')
test2 = str(y).find('.')
print(type(test))
print(test2)
