name_of_city = input()
deal_type = input()
vip_discount = input()
days_staying = int(input())

price = 0

if name_of_city == "Bansko" or name_of_city == "Borovets":
    if deal_type == "noEquipment":
        if vip_discount == "yes":
            price = (80 * 0.95) * days_staying
        elif vip_discount == "no":
            price = 80 * days_staying
    elif deal_type == "withEquipment":
        if vip_discount == "yes":
            price = (100 * 0.90) * days_staying
        elif vip_discount == "no":
            price = 100 * days_staying

elif name_of_city == "Varna" or name_of_city == "Burgas":
    if deal_type == "noBreakfast":
        if vip_discount == "yes":
            price = (100 * 0.93) * days_staying
        elif vip_discount == "no":
            price = 100 * days_staying
    elif deal_type == "withBreakfast":
        if vip_discount == "yes":
            price = (130 * 0.88) * days_staying
        elif vip_discount == "no":
            price = 130 * days_staying

else:
    print("Invalid input!")
    exit()


if days_staying < 1:
    print("Days must be positive number!")
    exit()
if days_staying > 7:
    price = price - price / days_staying

print(f"The price is {price:.2f}lv! Have a nice time!")