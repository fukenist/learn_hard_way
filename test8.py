i = 0
numbers = []
def call_while(til, inc):
	global i
	while i < til:
		print(f'At the top i is {i}')
		numbers.append(i)

		i+=inc

		print("Numbers now: ", numbers)
		print(f'At the bottom i is {i}')

#call_while(8,2)

def call_for(til, inc):
	for k in range(0,til):
		print(f'At the top i is {k}')
		numbers.append(k)

call_for(5, 1)
print("The numbers: ")

for num in numbers:
	print(num)	