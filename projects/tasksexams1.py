voucher_balance = int(input())
total_spent = 0
tickets_count = 0
other_products = 0

while True:
    product_name = input()
    if product_name == "End":
        break

    purchase_value = 0
    if len(product_name) > 8:
        purchase_value = ord(product_name[0]) + ord(product_name[1])
    else:
        purchase_value = ord(product_name[0])

    if voucher_balance >= purchase_value:
        total_spent += purchase_value
        voucher_balance -= purchase_value
        if len(product_name) > 8:
            tickets_count += 1
        else:
            other_products += 1
    else:
        break

print(tickets_count)
print(other_products)
