import random

def weekday():
	week = ['Wednesday', 'Friday', 'Saturday', 'Sunday', 'Thursday', 'Monday', 'Tuesday']
	return week[random.randint(0,len(week) - 1)]

def parents():
	where = ['home', 'work']
	return where[random.randint(0,len(where) - 1)]

teachers = ['Tew Rower', 'Teresa Poppins', 'Phil Collins', 'Omar Huyam', 'Silver Moon', 'Krup Gven', 'Ron Macaron', "Zen The Queen", "Fred Marine", 'Kilt Reddy', 'Mary Cropaly', 'Grey Worm', "Dead Poet", "Anet Obscure"]
marks = ['bad', 'not bad', 'great']

def subjects():
	list_of_subjects = [['Physics', marks[1], teachers[0]], ['Literature', marks[2], teachers[1]], ['Speech', marks[0], teachers[2]], ['Writing', marks[2], teachers[3]], ['Algebra', marks[2], teachers[4]], ['Geometry', marks[1], teachers[4]], ['Statistics', marks[1], teachers[5]], ['Trigonometry', marks[1], teachers[6]], ['Biology', marks[0], teachers[7]], ['Chemistry', marks[0], teachers[8]], ['Earth', marks[2], teachers[1]], ['Economics', marks[2], teachers[9]], ['Geography', marks[2], teachers[1]], ['History', marks[2], teachers[2]], ['Foreign Languages', marks[2], teachers[10]], ['Arts', marks[1], teachers[11]], ['Computer applications', marks[2], teachers[12]], ['Physical education', marks[0], teachers[13]]]
	schedule = list()

	for i in range(0,6):
		schedule.append(list_of_subjects[random.randint(0, len(list_of_subjects) - 1)])
	schedule.sort()
	return schedule

def in_school(lessons):
	print(f'First lesson: {lessons[0][0]}')
	print(f'Second lesson: {lessons[1][0]}')
	print(f'Third lesson: {lessons[2][0]}')
	print(f'Fourth lesson: {lessons[3][0]}')
	print(f'Fifth lesson: {lessons[4][0]}')

def question(lesson):
	#dictionary for subjects and tasks
	db_les = {'Physics': ['Speed of light is 300000 km/s. Distance from Earth to the Moon equals 384400 km.\nHow many seconds does it take light to go from Earth to Moon?\nRound your answer up', '2'], 'Literature': ['Who wrote Pride and Prejudice?', 'Jane Austen'], 'Speech': ['What is wrong with this word - beatiful.\nCorrect the mistake', 'beautiful'], 'Writing': ['Write how you passed your last summer? (use no less than 100 words'], 'Algebra': ['What is the answer of formula: ((10 + 25) / 7) * 10 - 47', '3'], 'Geometry': ['What equals PI number? (Round to the second number after the point)', '3.14'], 'Statistics': ['Write the missing word: There is a ..., big ... and statistics', 'lie'], 'Trigonometry': ['How many degrees is the right angle?', '90'], 'Biology': ['What animals group do dolphins belong to?', 'mamals'], 'Chemistry': ['Write formula of alcohol (ethanol)', 'c2h5oh'], 'Earth': ['Is it Earth bigger than Mars?', 'yes'], 'Economics': ["Who first said about 'invisible hand of market'?", 'adam smith'], 'Geography': ['What is the capital of USA?', 'washington'], 'History': ['When did the WW2 started (only year)?', '1939'], 'Foreign Languages': ['Write the name of most popular artificial language?', 'esperanto'], 'Arts': ["Who painted 'La persistencia de la memoria' (only last name)?", 'dali'], 'Computer applications': ['What is the name of first widely used program computer language?', 'fortran'], 'Physical education': ['How many pull ups do you do?']}
	#unusual tasks with open answer
	if lesson == 'Writing':
		print(f'{db_les[lesson][0]}')
		story = input('Write your story here: ')

		if len(story.split()) >= 100:
			print(f'You got grade 5 for good long story')
			print(f'Story\'s length {len(story.split())}')
			return 5
		else:
			print(f'You got grade 2 for story which was bad or not long enough')
			print(f'Story\'s length {len(story.split())}')
			return 2
	elif lesson == 'Physical education':
		print(f'{db_les[lesson][0]}')
		pullups = input('How many? ')

		if int(pullups) < 5:
			print(f'You got grade 2. You need to train better')
			return 2
		elif  5 < int(pullups) and int(pullups) < 10:
			print(f'You got grade 4. Good result')
			return 4
		elif int(pullups) > 10:
			print(f'You got grade 5. Great result. You are ready to go to army!')
			return 5
		else:
			print('You had to input only number')
	#tasks with fixed answer
	else:
		print(f'Teacher asked you to solve the exercise\n{db_les[lesson][0]}')
		answer = input('>')
		if answer == db_les[lesson][1].lower():
			print(f'You got grade 5 for right answer')
			return 5
		else:
			print(f'You got grade 2 for wrong answer')
			return 2
