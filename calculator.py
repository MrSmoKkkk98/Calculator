# Simple calculator
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

# first number for calculations
number_1 = int(input('Enter your first number: '))

# second number for calculations
number_2 = int(input('Enter your second number: '))

# Addition
if operation == '+':
    print('{} + {} ='.format(number_1, number_2), number_1 + number_2)

# Subtraction
elif operation == '-':
    print('{} - {} ='.format(number_1, number_2), number_1 - number_2)

# Multiplication
elif operation == '*':
    print('{} * {} ='.format(number_1, number_2), number_1 * number_2)

# Division
elif operation == '/':
    print('{} / {} ='.format(number_1, number_2), number_1 / number_2)

# Wrong operation
else:
    print('You have not typed a valid operator, please run the program again.')
