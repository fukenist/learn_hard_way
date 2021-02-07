the_count = [1,2,3,4,5]
fruits = ['oranges', 'lemons', 'apples', 'pineapples']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
	print(f'This is count {number}')

for fruit in fruits:
	print(f'These are {fruit}')

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it

for i in change:
	print(f'I got {i}')

# we can also build lists, first start with an empty one

elements = []
#range not includes last number
for i in range(0,10):
	print(f'Adding {i} to the list')
	elements.append(i)


# now we can print them out too
for el in elements:
	print(f'Element was : {el}')