month = input()
nights_count = int(input())

studios = 0
apartments = 0

if month == "May" or month == "October":
    studios = 50
    apartments = 65
elif month == "June" or month == "September":
    studios = 75.20
    apartments = 68.70
elif month == "July" or month == "August":
    studios = 76
    apartments = 77

if 7 < nights_count <= 14 and month == "May" or month == "October":
    studios *= 0.95
elif nights_count > 14 and month == "May" or month == "October":
    studios *= 0.70
elif nights_count > 14 and month == "June" or month == "September":
    studios *= 0.80

if nights_count > 14:
    apartments *= 0.90

print(f"Apartment: {nights_count * apartments:.2f} lv.")
print(f"Studio: {nights_count * studios:.2f} lv.")

