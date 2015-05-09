print("hello, world!")

num = 20
age = "I am %s years old."
print(age %num)

tuplefirst = (0, 1, 2, 3)
""" tuples are not rewriteable."""

list1 = ["When We Were Young", "Yellow"]
list2 = ["Fifth Element", "Gattaca"]

list1 = list1 + list2
list1.append("white fang")
print(list1)

print(20 - 10 + 3 + 15-5  + (3 * 15))

FirstName = input("insert first name ")
LastName = input ("Insert last name ")


print("Hello there, %s %s" %(FirstName, LastName))

for i in range(0, 29, 2):
	print(i)
	
day = "monday"
if day == "monday":
	print ("today it will rain")
else:
	print ("today is sunny")
	
weight = 200.0
moonweight = 200.0 * (1.0/6.0)
gain = 1.0 * (1.0/6.0)
for i in range(0, 10):
	weight = weight + 1
	moonweight = moonweight + gain
	print (weight)
	print (moonweight)