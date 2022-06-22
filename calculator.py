# Simple calculator
# Define welcome function
def welcome():
    print('''
Welcome to the calculator!''')

# Define calculate function


def calculate():
    operation = input('''Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
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

# Power
    elif operation == '**':
        print('{} ** {} ='.format(number_1, number_2), number_1 ** number_2)

# Modulo
    elif operation == '%':
        print('{} % {} ='.format(number_1, number_2), number_1 % number_2)

# Wrong operation
    else:
        print('You have not typed a valid operator, please run the program again.')


# Add again function to calculate() function
    again()


# Define again() function to ask user if they want to use the calculator again


def again():

    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()


# Call welcome() outside of the function
welcome()
# Call calculate() outside of the function
calculate()
