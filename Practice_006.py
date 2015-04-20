from statistics import mean as average

admins = {'Python':'Pass123', 'user2':'pass2'}

studentDict = {'Jeff':[78, 88, 93], 
				'Alex':[92, 49, 55], 
				'Sam':[32, 68, 99]}

def enterGrades():
	nameToEnter = input('Student Name: ' )
	gradeToEnter = input('Grade: ')
	
	if nameToEnter in studentDict:
		print('Adding Grade...')
		studentDict[nameToEnter].append(float(gradeToEnter))
	else: 
		print('Student Does not exist.')
	print(studentDict)
	
def removeStudent():
	nameToRemove = input('What student to remove?: ')
	if nameToRemove in studentDict:
		print('removing student...')
		del studentDict[nameToRemove]
	
	print(studentDict)

def studentAVGs():
	for eachStudent in studentDict:
		gradeList = studentDict[eachStudent]
		avgGrade = average(gradeList)
		print (eachStudent, 'has an average grade of:', avgGrade)
	

	
def main():
	print("""
	Welcome to Grade Central
	
	[1] - Enter Grades
	[2] - Remove Student
	[3] - Student Average Grades
	[4] - Exit
	""")
	action = input ('What would you like to do today? (Enter a number)')
	if action == '1':
		enterGrades()
	elif action == '2':
		removeStudent()
	elif action  == '3':
		studentAVGs()
	else:
		exit()
		
login = input('UserName: ')
passw = input('Password: ')

if login in admins:
	if admins[login] == passw:
		print('Welcome, ', login)
		while True:
			main()
	else:
		print('invalid pass')
else:
	print('no such user')