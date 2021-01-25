form = '{} {} {} {}'

print(form.format('1','2','3','4'))

print(form.format(True, False, True, True))

print(form.format(form, form, form, form))

print(form.format("\nDon't be afraid\n","To look like a fool\n","If you are\n","You will be one\n"))

print("""What
The Hell
Is going on """)

print('Go\a')
print('Here\b')
print('Bitch\f')
print('Wow\r')
print('To\v')

print('How old are you?', end=' ')
age = input()
print('How many times you\'ve been loved in?', end=' ')
times = input()
print('What is the square of cube?', end=' ')
ans = input()

print(f'So you are {age} years old, slept with {times} people and have no idea what is square of a cube? {ans}')