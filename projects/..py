minutes = int(input())
count_walks = int(input())
calories_daily = int(input())


total_time_walk = minutes * count_walks
total_calories = total_time_walk * 5

if calories_daily * 0.50 < total_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day:{total_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories}.")
