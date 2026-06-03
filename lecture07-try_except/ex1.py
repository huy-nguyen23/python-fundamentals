a=input('Please enter your age: ')
try:
    age=int(a)
    print(f'Thank you. Your age is {age}.')
except ValueError:
    print('Error: Please enter a valid whole number for your age.')