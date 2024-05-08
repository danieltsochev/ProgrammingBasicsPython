people_count = int(input())
season = input()

total_price_b_d = 0
total_price = 0

if season == "spring":
    if people_count <= 5:
        total_price = people_count * 50.00
    else:
        total_price = people_count * 48.00

elif season == "summer":
    if people_count <= 5:
        total_price_b_d = people_count * 48.50
    else:
        total_price_b_d = people_count * 45.00
    total_price = total_price_b_d * 0.85

elif season == "autumn":
    if people_count <= 5:
        total_price = people_count * 60.00
    else:
        total_price = people_count * 49.50

elif season == "winter":
    if people_count <= 5:
        total_price_b_d = people_count * 86.00
    else:
        total_price_b_d = people_count * 85.00
    total_price = total_price_b_d * 1.08

print(f"{total_price:.2f} leva.")


