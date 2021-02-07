import school_week

day = school_week.weekday()
where = school_week.parents()
schedule = school_week.subjects()

marks_for_day = {}
money = {'rubles': 0}

print(f"You woke up with alarm. It is 7 a.m {day}")
print(f"Your parents at {where} ")
print(f'Today you have 5 lessons:')
print(f'You were given 200 rubles pocket money')
money['rubles'] = 200
print(money)

#for i in range(len(schedule)):
	#print(schedule[i][0])

print(f'Where are you going to?')
print(f'- school')
print(f'- videosalon')
print(f'- friends')
print(f'- stay home')

choose = input('>')

if choose == 'stay home' and where == 'home':
	print('Your parents won\'t be happy seeing at you staying home so get out')
	print('You had to go to school')
	school_week.in_school(schedule)
elif choose == 'stay home' and where == 'work':
	print(f"You can stay home")
elif choose == 'school':
	print("You decided to go right to school")
	
	school_week.in_school(schedule)
	first = schedule[0][0]
	second = schedule[1][0]
	third = schedule[2][0]
	fourth = schedule[3][0]
	fifth = schedule[4][0]
	
	print(f'First lesson is {first}.\nYou have {schedule[0][1]} marks on it. {schedule[0][2]} is your teacher')
	marks_for_day[first] = school_week.question(first)

	print(f'Second lesson is {second}.\nYou have {schedule[1][1]} marks on it. {schedule[1][2]} is your teacher')
	marks_for_day[second] = school_week.question(second)

	print(f'Third lesson is {third}.\nYou have {schedule[2][1]} marks on it. {schedule[2][2]} is your teacher')
	marks_for_day[third] = school_week.question(third)

	print(f'Fourth lesson is {fourth}.\nYou have {schedule[3][1]} marks on it. {schedule[3][2]} is your teacher')
	marks_for_day[fourth] = school_week.question(fourth)

	print(f'Fifth lesson is {fifth}.\nYou have {schedule[4][1]} marks on it. {schedule[4][2]} is your teacher')
	marks_for_day[fifth] = school_week.question(fifth)

	print(f'After lessons you with friends came to the stall.\n What did you decide to buy?')
	print(f'1. sweets - 50 rubles\n2. pastry - 100\n3.beer, cigarettes\n')
	choice = input('Please, type a number of choice>')

	if choice == '1':
		money['rubles'] = money['rubles'] - 50
		print(f'You have some sweets now.')
	elif choice == '2':
		money['rubles'] = money['rubles'] - 100
		print(f'You have some pastry. Tasty one!')
	elif choice == '3':
		money['rubles'] = money['rubles'] - 200
		print(f'Your ass is in great danger!')
	else:
		print(f'You asked some shit that wasn\'t there so you went out didn\'t buy anything')

	print(f'You returned home and when parents came from work they asked you about marks for day')
	print(f'You showed yours and ')
	print(sum(marks_for_day.values()))
	if int(sum(marks_for_day.values())) < 19:
		print(f'Mom weren\'t happy after seeing your marks')
	elif int(sum(marks_for_day.values())) > 19:
		print(f'Mom eulogized you for your marks')
	else:
		print(f'You lost your school journal. Again')

	print(f'You have ')
	for i in money:
		print(f'{money[i]} rubles left')

elif choose == 'videosalon':
	print(f'You went to videosalon and were playing Cyphon Filter on ps2 all day')
	print(f'When mom asked you about marks you said that lost your school journal. Again')
	money['rubles'] = money['rubles'] - 200
	print(f'You have ')
	for i in money:
		print(f'{money[i]} rubles left')

elif choose == 'friends':
	print(f'You went to your friend\'s home and we were playing fifa all day')
	print(f'When mom asked you about marks you said that lost your school journal. Again')
	print(f'You have ')
	for i in money:
		print(f'{money[i]} rubles left')
else:
	print(f'Your choice is obscure as you are')
