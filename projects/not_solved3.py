from math import ceil

h = int(input())
w = int(input())
minus_percent = int(input())

all_area_bm = (h * w) * 4
all_area = ceil(all_area_bm - (all_area_bm * minus_percent) / 100)
painted_are = 0

while all_area >= painted_are:
    litres_paint = input()

    if litres_paint == "Tired!":
        break

    painted_are += int(litres_paint)

if all_area > painted_are:
    print(f"{all_area - painted_are} quadratic m left.")
elif painted_are > all_area:
    print(f"All walls are painted and you have {abs(painted_are - all_area)} l paint left! ")
else:
    print("All walls are painted! Great job, Pesho!")