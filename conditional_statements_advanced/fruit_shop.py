type_fruit = input()
day_of_week = input()
quantity = float(input())

price = 0

correct_data = True

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday'\
    or day_of_week == 'Thursday' or day_of_week == 'Friday':
    if type_fruit == 'banana':
        price = 2.50
    elif type_fruit == 'apple':
        price = 1.20
    elif type_fruit == 'orange':
        price = 0.85
    elif type_fruit == 'grapefruit':
        price = 1.45
    elif type_fruit == 'kiwi':
        price = 2.70
    elif type_fruit == 'pineapple':
        price = 5.50
    elif type_fruit == 'grapes':
        price = 3.85
    else:
        correct_data = False

elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if type_fruit == 'banana':
        price = 2.70
    elif type_fruit == 'apple':
        price = 1.25
    elif type_fruit == 'orange':
        price = 0.90
    elif type_fruit == 'grapefruit':
        price = 1.60
    elif type_fruit == 'kiwi':
        price = 3.00
    elif type_fruit == 'pineapple':
        price = 5.60
    elif type_fruit == 'grapes':
        price = 4.20
    else:
        correct_data = False
else:
    correct_data = False

if correct_data:
    print(f'{quantity * price:.2f}')
else:
    print('error')


