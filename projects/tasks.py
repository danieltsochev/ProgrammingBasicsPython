eggs_in = int(input())

sold_eggs = 0

action = input()

while action != "Close":
    current_eggs = int(input())

    if action == "Buy":
        if current_eggs > eggs_in:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_in}.")
            break
        else:
            eggs_in -= current_eggs
            sold_eggs += current_eggs

    elif action == "Fill":
        eggs_in += current_eggs

    action = input()

if action == "Close":
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")


































































































































































