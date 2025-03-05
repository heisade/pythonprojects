# This is a remake of the first calculator i made
# So i need to create a calculator that can do the basic arithmetic calculation
import math


print("====== WELCOME TO MY CALCULATOR 2.0 ======")

calculator_type = input('Basic Calculator: Enter [1]\n'
                       'Intermediate Calculator: Enter [2]\n'
                       'Advanced calculator: Enter [3]\n'
                       'Enter the type of calculator you want to use: ')        # Different types of calculators

# Breaking calculator into multiple types which are
#Basic calculator, intermediate calculator and advanced calculator
# And i need to do better naming my calulator types



if calculator_type == '1':
    first_number = float(input("Enter First number: "))       # First input number
    second_number = float(input("Enter Second number: "))     # Second input number
    operator = input('Enter the Operator [+ - * /]: ')

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y
    
    def divide(x, y):
        return x / y

    operators = {'*': multiply, '+': add, '-': subtract, '/': divide}

    # Check if operator is valid
    
    if operator not in operators:
        print("Invalid operator! Please use one of [+ - * /].")
    
    else:
        if operator == '+':
            print(f"The addition of {first_number} and {second_number} is {add(first_number, second_number)}")
        
        elif operator == '-':
            print(f"The subtraction of {first_number} and {second_number} is {subtract(first_number, second_number)}")
            
        elif operator == '*':
            print(f"The multiplication of {first_number} and {second_number} is {multiply(first_number, second_number)}")
            
        else:
            if second_number == 0:
                print('Error: Division by zero')
            else:
                print(f"The division of {first_number} and {second_number} is {divide(first_number, second_number)}")
    

elif calculator_type == '2':
    sub_calculator_type = input('Enter [1] for Trigonometric\n'
                                'Enter [2] for Exponentiation and roots\n'
                                'Enter [3] for Logarithmic functions\n'
                                'Enter number: ')
    
    if sub_calculator_type == '1':
        trigonometric = input('Enter [1] for sine(sin)\n'
                              'Enter [2] for cosine(cos)\n'
                              'Enter [3] for Tangent(tan)\n'
                              'Enter number: ')
        
        def trigonometry_sine(opposite, hypotenus):
            sine = opposite / hypotenus
            return f"The Sine is {sine}"
        
        def trigonometry_cos(adjacent, hypotenus):
            cosine = adjacent / hypotenus
            return f"The Cos is {cosine}"
        
        def trigonometry_tan(opposite, adjacent):
            tangent = opposite / adjacent
            return f"The Tan is {tangent}"

        trigonometry = {'1': trigonometry_sine, '2':trigonometry_cos, '3': trigonometry_tan}
    
        if trigonometric not in trigonometry:   
            print("Invalid Input!")             # To see if trigonometric input is valid
        else:
            if trigonometric == '1':
                opposite = float(input("Enter Opposite: "))
                hypotenus = float(input("Enter Hypotenus: "))
                print(trigonometry_sine(opposite, hypotenus))
            elif trigonometric == '2':
                adjacent = float(input("Enter Adjacent: "))
                hypotenus = float(input("Enter Hypotenus: "))
                print(trigonometry_cos(adjacent, hypotenus))
            else:
                opposite = float(input("Enter Opposite or Sine: "))
                adjacent = float(input("Enter Adjacent or Cos: "))
                print(trigonometry_tan(opposite, adjacent))


    elif sub_calculator_type == '2':
        exponential_and_root = input('Enter [1] for exponential\n'
                                     'Enter [2] for roots\n'
                                     'Enter number: ')

        def exponential(x, y):
            return x ** y

        def root(x, y):
            return x ** 1/y

        expo_and_root = {'1': exponential, '2': root}

        if exponential_and_root not in expo_and_root:       # For invalid input
            print('Invalid input! try again')
        else:
            if exponential_and_root == '1':
                expo_number = float(input('Enter number: '))
                expo = float(input('Enter exponential: '))
                print(f"The {expo} exponential of {expo_number} is {exponential(expo_number, expo)}")

            else:
                root_number = float(input('Enter number: '))
                roots = float(input('Enter root: '))
                print(f"The {roots} root of {root_number} is {root(root_number, roots)}")

    elif sub_calculator_type == '3':
        logarithmic_function =input('Enter [1] for logarithm to base 10\n'
                                    'Enter [2] to natural log\n'
                                    'Enter number: ')

        def log10(x):
            return math.log10(x)
        
        def natural_log(x):
            return math.log(x)

        logs = {'1': log10, '2': natural_log}

        if logarithmic_function not in logs:
            print("Invalid input!")
        else:
            if logarithmic_function == '1':
                log10_number = float(input("Enter number: "))
                print(f'The base 10 of {log10_number} is {log10(log10_number)}')
            else:
                natural_log_number = float(input("Enter number: "))
                print(f'The natural log of {natural_log_number} is {natural_log(natural_log_number)}')

    
elif calculator_type == '3':
    sub_calculator_type = input('Enter [1] for Unit converstion\n'
                                  'Enter [2] for Currency converter\n'
                                  'Enter number: ')
    if sub_calculator_type == '1':
        unit_conversion = input('Enter [1] for Kilometer to miles\n'
                                 'Enter [2] for miles to kilometers\n'
                                 'Enter [3] for grams to kilograms\n'
                                 'Enter [4] for kilograms to grams\n'
                                 'Enter [5] for kilograms to tons\n'
                                 'Enter [6] for Celcius to Fahrenheit\n'
                                 'Enter [7] for Fahrenheit to Celcius\n'
                                 'Enter number: ')

        def km_to_miles(x):
            miles = x * 0.62137
            return f'{x} kilometers is {miles} miles.'
        
        def miles_to_km(x):
            km = x / 0.62137
            return f'{x} miles is {km} kilometers.'
        
        def grams_to_kg(x):
            kg = x * 1000
            return f'{x} grams is {kg} kilometers.'
        
        def kg_to_grams(x):
            grams = x / 1000
            return f'{x} kilograms is {grams} grams.'

        def kg_to_ton(x):
            ton = x * 1000
            return f'{x} kilograms is {ton} tons.'
        
        def celcius_to_fahrenheit(x):
            fahrenheit = (9/5*x)+32
            return f'{x} celcius is {fahrenheit} fahrenheit.'

        def fahrenheit_to_celcius(x):
            celcius = (5/9)*(x-32)
            return f'{x} fahrenheit is {celcius} celcius.'

        units = {'1': km_to_miles,
                 '2': miles_to_km,
                 '3': grams_to_kg,
                 '4': kg_to_grams,
                 '5': kg_to_ton,
                 '6': celcius_to_fahrenheit,
                 '7': fahrenheit_to_celcius}

        if unit_conversion not in units:
            print("Invalid input!")
        else:
            if unit_conversion == '1':
                km = float(input('Enter kilometers: '))
                print(km_to_miles(km))
            elif unit_conversion =='2':
                miles = float(input('Enter miles: '))
                print(miles_to_km(miles))
            elif unit_conversion == '3':
                grams = float(int('Enter grams: '))
                print(grams_to_kg(grams))
            elif unit_conversion == '4':
                kg = float(input('Enter Kilogram: '))
                print(kg_to_grams(kg))
            elif unit_conversion == '5':
                kg = float(input('Enter kilogram: '))
                print(kg_to_ton(kg))
            elif unit_conversion == '6':
                celcius = float(input('Enter Celcius: '))
                print(celcius_to_fahrenheit(celcius))
            else:
                fahrenheit = float(input('Enter Fahrenheit: '))
                print(fahrenheit_to_celcius(fahrenheit))
            
