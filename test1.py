def add(a,b):
	print(f'Adding {a} and {b}')
	return a + b

def subtract(a,b):
	print(f'Subtract {a} and {b}')
	return a - b

def multiply(a,b):
	print(f'Multiply {a} on {b}')
	return a * b	

def divide(a,b):
	print(f'Divide {a} on {b}')
	return a / b

print("Let's do some math with just functions!")

age = add(20,50)
height = subtract(170,3)	
weight = multiply(20,8)	
iq = divide(300,2)

print(f'Age {age} Height {height} Weight {weight} Iq {iq}')

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
what1 = height - (divide(iq,2) * weight) + age 
print('I said:', what, 'are you laughing at?')
print('I said:', what1, 'are you laughing at mf?')

frml = (height * weight) / iq + age
frml1 = add(age, divide(multiply(height,weight), iq))

print(frml)
print(frml1)