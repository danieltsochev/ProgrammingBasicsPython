days_of_stay = int(input()) - 1
type_of_place = input()
rating = input()

price = 0


ROOM_FOR_ONE_PERSON_P_N = 18.00
APARTMENT_P_N = 25.00
PRESIDENT_APARTMENT_P_N = 35.00

if type_of_place == "room for one person":
    price = days_of_stay * ROOM_FOR_ONE_PERSON_P_N

elif type_of_place == "apartment":
    if days_of_stay < 10:
        price = (days_of_stay * APARTMENT_P_N) * 0.70
    elif 10 <= days_of_stay <= 15:
        price = (days_of_stay * APARTMENT_P_N) * 0.65
    elif days_of_stay > 15:
        price = (days_of_stay * APARTMENT_P_N) * 0.50

elif type_of_place == "president apartment":
    if days_of_stay < 10:
        price = (days_of_stay * PRESIDENT_APARTMENT_P_N) * 0.90
    elif 10 <= days_of_stay <= 15:
        price = (days_of_stay * PRESIDENT_APARTMENT_P_N) * 0.85
    elif days_of_stay > 15:
        price = (days_of_stay * PRESIDENT_APARTMENT_P_N) * 0.80

if rating == "positive":
    price *= 1.25
elif rating == "negative":
    price *= 0.90

print(f"{price:.2f}")






