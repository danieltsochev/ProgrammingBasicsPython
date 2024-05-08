total_price = 0

days_count = int(input())
hours_count = int(input())

for day in range(1, days_count + 1):
    price = 0

    for hour in range(1, hours_count + 1):

        if day % 2 == 0 and hour % 2 != 0:
            price += 2.50
            total_price += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            price += 1.25
            total_price += 1.25
        else:
            price += 1
            total_price += 1

    print(f"Day: {day} - {price:.2f} leva")
print(f"Total: {total_price:.2f} leva")