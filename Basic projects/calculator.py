print('==== WELCOME TO MY CALCULATOR ====')
name = input('Please enter your name: ')
print('Welcome', name + '. Please input the numbers below.')

first_number = float(input('Enter first number: '))
second_number = float(input('Enter Second number: '))

operator = input('Enter the operator[+ - * /]: ')

if operator == '+':
    print(first_number + second_number)

elif operator == '-':
    print(first_number - second_number)

elif operator == '*':
    print(first_number * second_number)

elif operator == '/':
    print(first_number / second_number)

else:
    print('Invalid Input')