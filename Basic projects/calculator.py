import math
print('==== WELCOME TO MY CALCULATOR ====')
calculator_type= input('Basic Calculator: Type[1]\n'
                       'Intermediate Calculator: Type[2]\n'
                       'Advanced calculator: Type[3]\n'
                       'Enter the type of calculator you want to use: ')
name = input('Please enter your name: ')
print('Welcome', name + '. Please input the numbers below.')

if calculator_type == '1':
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

elif calculator_type == '2':
    sub_calculator_type = input('Enter [1] for Trigonometric\n'
                                'Enter [2] for Exponentiation and roots\n'
                                'Enter [3] for Logarithmic functions\n'
                                'Enter number: ')
    
    if sub_calculator_type == '1':
        trigonometric = input('Enter [1] for sine(sin)\n'
                              'Enter [2] for cosine(cos)\n'
                              'Enter [3] for Tangent(tan)'
                              'Enter number: ')
        
        if trigonometric == '1':
            for_sine_1 = int(input('Enter Opposite: '))
            for_sine_2 = int(input('Enter Hypotenus: '))
            sine = for_sine_1 / for_sine_2
            print('The sine is', sine)
        elif trigonometric == '2':
            for_cosine_1 = int(input('Enter Adjacent: '))
            for_cosine_2 = int(input('Enter Hypotenus: '))
            cosine = for_cosine_1 / for_cosine_2
            print('The cosine is', cosine)
        elif trigonometric == '3':
            for_tangent_1 = int(input('Enter Opposite or sine: '))
            for_tangent_2 = int(input('Enter Ajacent or cos: '))
            tangent = for_tangent_1 / for_tangent_2
            print('The tangent is', tangent)

    elif sub_calculator_type == '2':
        exponential_and_root = input('Enter [1] for exponential\n'
                                     'Enter [2] for roots\n'
                                     'Enter number: ')
        
        if exponential_and_root == '1':
            for_exponential_1 = int(input('Enter number: '))
            for_exponential_2 = int(input('Enter exponential: '))
            exponential = for_exponential_1 ** for_exponential_2
            print('The the annswer is', exponential)

        elif exponential_and_root == '2':
            for_root_1 = int(input('Enter number: '))
            for_root_2 = int(input('Enter root: '))
            root = for_root_1 ** (1/for_root_2)
            print('The root of', for_root_1, 'is', root)

    elif sub_calculator_type == '3':
        logarithmic_function =input('Enter [1] for logarithm to base 10\n'
                                    'Enter [2] to natural log\n'
                                    'Enter number: ')

        if logarithmic_function == '1':
            base_1 = int(input('Enter number: '))
            log_base_10 = math.log10(base_1)
            print('The base 10 of', base_1, 'is', log_base_10)

        elif logarithmic_function == '2':
            natural_log_number = int(input('Enter number: '))
            natural_log = math.log(natural_log_number)

elif calculator_type == '3':
    sub_calculator_type_2 = input('Enter [1] for Unit converstion\n'
                                  'Enter [2] for Currency converter\n'
                                  'Enter number: ')
    if sub_calculator_type_2 == '1':
        sub_sub_calculator = input('Enter [1] for Kilometer to miles\n'
                                   'Enter [2] for miles to kilometers\n'
                                   'Enter [3] for grams to kilograms\n'
                                   'Enter [4] for kilograms to grams\n'
                                   'Enter [5] for kilograms to tons\n'
                                   'Enter [6] for Celcius to Fahrenheit\n'
                                   'Enter [7] for Fahrenheit to Celcius\n'
                                   'Enter number: ')
        if sub_sub_calculator == '1':
            for_km = int(input('Enter kilometers: '))
            km = for_km * 0.62137
            print(for_km, 'kilometers is', km, 'miles.')

        elif sub_sub_calculator == '2':
            for_miles = int(input('Enter miles: '))
            km = for_miles / 0.62137
            print(for_miles + 'miles is', km, 'kilometers.')

        elif sub_sub_calculator == '3':
            grams = int(input('Enter grams: '))
            kg = grams * 1000
            print(grams + 'grams is', kg, 'kilograms' )

        elif sub_sub_calculator == '4':
            kg = int(input('Enter Kilogram: '))
            grams = kg / 1000
            print(kg + 'kilograms is', grams, 'grams')

        elif sub_sub_calculator == '5':
            kg = int(input('Enter kilograms: '))
            tons = kg / 1000
            print(kg , 'kg is', tons, 'tons')

        elif sub_sub_calculator == '6':
            celcius = int(input('Enter celcuis: '))
            fahrenheit = (9/5*celcius)+32
            print(celcius + 'C is', fahrenheit + 'fahrenheit')

        elif sub_sub_calculator == '7':
            fahrenheit = int(input('Enter Fahrenheit: '))
            celcius = (5/9) * (fahrenheit - 32)
            print(fahrenheit, 'Fahrenheit is', celcius, 'celcuis')

        else:
            print('Invalid Input.')

    elif sub_calculator_type_2 == '2':
        print('Coming soon!! Stay tuned')

    else:
        print('Invalid Input.')

else:
        print('Invalid Input.')








        


        
