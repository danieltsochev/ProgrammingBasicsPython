type_flowers = input()
flowers_count = int(input())
budget = int(input())

ROSES_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

total_price = 0

if type_flowers == 'Roses':
    total_price = flowers_count * ROSES_PRICE

    if flowers_count > 80:
        total_price *= 0.80

elif type_flowers == 'Dahlias':
    total_price = flowers_count * DAHLIAS_PRICE

    if flowers_count > 90:
        total_price *= 0.85

elif type_flowers == 'Tulips':
    total_price = flowers_count * TULIPS_PRICE

    if flowers_count > 80:
        total_price *= 0.85

elif type_flowers == 'Narcissus':
    total_price = flowers_count * NARCISSUS_PRICE

    if flowers_count < 120:
        total_price *= 1.15

elif type_flowers == 'Gladiolus':
    total_price = flowers_count * GLADIOLUS_PRICE

    if flowers_count < 80:
        total_price *= 1.20

if total_price <= budget:
    print(f'Hey, you have a great garden with {flowers_count} {type_flowers} and {budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money, you need {total_price - budget:.2f} leva more.')

