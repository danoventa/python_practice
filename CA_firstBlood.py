
anInt = 123
aString = 'Come and show me another city with lifted head singing so proud to be alive and coarse and strong and cunning...proud to be Hog Butcher, Tool Maker, Stacker of Wheat, Player with Railroads and Freight Handler to the Nation.'
aList = [1, 2, 3]

''' int to list, not converting to string '''
def intToList(sentInt):
	tempList = []
	while sentInt > 0:
		tempList.append(sentInt%10)
		sentInt /= 10
		
	tempList.reverse()
	print (tempList)
	
''' any instance of and '''	
def howManyAnds(sentString):
	count = 0
	while sentString.find("and") != -1:
		count = count + 1 
		sentString = sentString[sentString.find("and") + 1:]
	print (count)
	
''' stricter, only "and" '''	
def howManyAndsStrict(sentString):
	count = 0
	while sentString.find("and") != -1 and sentString[sentString.find("and") -1] == " " and sentString[sentString.find("and") + 3] == " ":
		count = count + 1 
		sentString = sentString[sentString.find("and") + 1:]
	print (count)
	
''' list to a palindrom list '''	
def listToPalindrome(sentList):
	tempList = []
	for item in sentList:
		tempList.append(item)
	tempList.reverse()
	newList = sentList + tempList
	print (newList)

def main():
	intToList(anInt)
	howManyAnds(aString)
	howManyAndsStrict(aString)
	listToPalindrome(aList)
	
	

if __name__ == "__main__":
    main()