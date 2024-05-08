hall_rent = float(input())

CAKE_PRICE = hall_rent * 0.20
DRINKS_PRICE = CAKE_PRICE - CAKE_PRICE * 0.45
ANIMATOR_PRICE = hall_rent / 3

total_budget = hall_rent + CAKE_PRICE + DRINKS_PRICE + ANIMATOR_PRICE

print(total_budget)