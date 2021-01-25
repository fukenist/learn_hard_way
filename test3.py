start = 10902

print('This is format: {}'.format(start))

def ut(numba):
	first = 100 * 56
	second = first / 15
	third = second - first

	return first, second, third

formula = ut(start)
first, second, third = formula
print(first)
#answers from func ut returned in formula
print('This is {} which is not {} but both of them {}'.format(*formula))