cats_count = int(input())

small_cats = 0
big_cats = 0
large_cats = 0

food_amount = 0
food_price = 0

for _ in range(cats_count):
    food = float(input())

    food_amount += food

    if 100 <= food < 200:
        small_cats += 1
    elif 200 <= food < 300:
        big_cats += 1
    elif 300 <= food < 400:
        large_cats += 1

food_price = (food_amount / 1000) * 12.45

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {large_cats} cats.")
print(f"Price for food per day: {food_price:.2f} lv.")