budget = float(input())

product_count = 0
monet_spend = 0
current_budget = float(budget)
last_pr_price = 0
while True:
    name_of_pr = input()
    if name_of_pr == "Stop":
        break
    product_count += 1

    price_of_pr = float(input())

    if product_count % 3 == 0 and product_count != 0:
        price_of_pr *= 0.50
    monet_spend += price_of_pr
    current_budget -= price_of_pr
    last_pr_price = price_of_pr

    if price_of_pr > current_budget:
        break


if last_pr_price <= current_budget:
    print(f"You bought {product_count} products for {monet_spend:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {abs(current_budget):.2f} leva!")