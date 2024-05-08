adults = 0
kids = 0
money_toys = 0
money_sweaters = 0

while True:
    age = input()

    if age == "Christmas":
        break

    if int(age) > 16:
        adults += 1
        money_sweaters += 15

    elif int(age) <= 16:
        kids += 1
        money_toys += 5

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {money_toys}")
print(f"Money for sweaters: {money_sweaters}")






