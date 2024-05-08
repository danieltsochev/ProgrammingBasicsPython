chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

CHICKEN_PRICE = 10.35
FISH_PRICE = 12.40
VEGETARIAN_PRICE = 8.15
DELIVERY_PRICE = 2.50

menus_price = \
    (chicken_menus * CHICKEN_PRICE) + \
    (fish_menus * FISH_PRICE) + \
    (vegetarian_menus * VEGETARIAN_PRICE)

desert_price = menus_price * 0.20

total_price = menus_price + desert_price + DELIVERY_PRICE

print(total_price)