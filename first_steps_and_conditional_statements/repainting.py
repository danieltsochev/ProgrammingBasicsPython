nylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5
BAGS_PRICE = 0.40

nylon += 2
paint += paint * 0.10
materials_price = (nylon * NYLON_PRICE) + \
                  (paint * PAINT_PRICE) + \
                  (thinner * THINNER_PRICE) + \
                  BAGS_PRICE
price_for_one_hour_of_work = materials_price * 0.30
total_price = materials_price + (price_for_one_hour_of_work * work_hours)

print(total_price)
