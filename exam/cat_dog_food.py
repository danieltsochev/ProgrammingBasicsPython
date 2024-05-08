days_count = int(input())
all_food_amount = float(input())

biscuits_eaten = 0
all_food_eaten = 0
dog_eaten = 0
cat_eaten = 0

for day in range(1,days_count + 1):
    dog = int(input())
    cat = int(input())

    if day % 3 == 0 and day != 0:
        biscuits_eaten = int(dog) + int(cat)

    dog_eaten += int(dog)
    cat_eaten += int(cat)
    all_food_eaten = dog_eaten + cat_eaten


print(f"bsc {biscuits_eaten * 0.10}")
print(f"all {all_food_eaten / all_food_amount * 100}")
print(f"d {dog_eaten / all_food_eaten * 100}")
print(f"c {cat_eaten / all_food_eaten * 100}")


