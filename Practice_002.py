def website(font, background_color, font_size, font_color):
	print('font:', font)
	print('bg:', background_color)
	print('Font size:', font_size)
	print('Font color:', font_color)

def website2(font='tnr', background_color='white', font_size='11', font_color='black'):
	print('font:', font)
	print('bg:', background_color)
	print('Font size:', font_size)
	print('Font color:', font_color)

def addition(num1, num2, num3, num4):
	answer = num1+num2+num3+num4
	return answer

def example():
	x = addition(5, 6, 7, 8)
	y = 3
	print(x+y)
	
	if x < y:
		print(x, 'is less than', y)

example ()
website('black', 'tnr', 'white', '11')
website(font_color='black', font='tnr', background_color='white', font_size='11')
website2()