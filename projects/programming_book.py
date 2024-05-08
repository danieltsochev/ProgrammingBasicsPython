price_for_page = float(input())
price_for_cover = float(input())
percen_discount = int(input())
designer_money = float(input())
percent_staff_pay = int(input())

first_bill = (price_for_page * 899) + (price_for_cover * 2)
second_bill = first_bill - (first_bill * percen_discount) / 100
third_bill = second_bill + designer_money
final_bill = third_bill - (third_bill * percent_staff_pay) / 100

print(f"Avtonom should pay {final_bill:.2f} BGN.")