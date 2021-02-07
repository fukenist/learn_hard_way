from sys import exit

def gold_room():
	print("This room is full of shit. How long could you be there?")
	
	choice = input('> ')
	if choice.isnumeric():
		how_long = int(choice)
		
	else:
		dead("Man, write a number")	

	if how_long < 50:
		print("Do you understand how stinky you will be after?")
		exit(0)

	else:
		dead("You sick bastard!")

def hroom_room():
	print("There is not light in this room")
	print("And you hear some noises")
	print("You need to find the exit")
	print("How would you use your inner vision?")
	inner_eye = False

	while True:
		choice = input('> ')

		if choice == "sleep":
			dead("It was so cold there that you couldn't")

		elif choice == 'meditate' and not inner_eye:
			print("You could out of your body and see the exit")
			inner_eye = True

		elif choice == 'meditate' and inner_eye:
			dead("You could not concentrate and failed")

		elif choice == "open door" and inner_eye:
			gold_room()

		else:
			dead("WTF")

def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")

	choice = input('> ')

	if 'flee' in choice:
		start()

	elif "head" in choice:
		dead("Well that was tasty")

	else:
		cthulhu_room()

def dead(why):
	print(why, "Good job!")
	exit(0)		

def start():
	print("Do you flee for your life or eat your head?")
	print("There is a door to your right and left.")
	print("Which one do you take?")

	choice = input('> ')

	if choice == 'left':
		hroom_room()

	elif choice == 'right':
		cthulhu_room()

	else:
		dead("You stumble around until rising")

start()

