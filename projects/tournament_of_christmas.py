days = int(input())

total_money = 0
total_wins = 0

for day in range(1, days+1):
    daily_money = 0
    daily_wins = 0

    while True:
        game = input()

        if game == "Finish":
            break

        result = input()

        if result == "win":
            daily_money += 20
            daily_wins += 1

    total_money += daily_money
    total_wins += daily_wins

    if daily_wins > len(game) / 2:
        total_money *= 1.1

if total_wins > days / 2:
    total_money *= 1.2

if total_wins > days / 2:
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
