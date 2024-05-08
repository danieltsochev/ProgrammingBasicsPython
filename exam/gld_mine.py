location = int(input())

for _ in range(location):
    gold_expected = float(input())
    days = int(input())
    amount_of_gold = 0
    average_of_gold = 0

    for _ in range(days):
        daily_gold = float(input())

        amount_of_gold += daily_gold
        average_of_gold = amount_of_gold / days

    if average_of_gold >= gold_expected:
        print(f"Good job! Average gold per day: {average_of_gold:.2f}.")
    else:
        print(f"You need {gold_expected - average_of_gold:.2f} gold.")