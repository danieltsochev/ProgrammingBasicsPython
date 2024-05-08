from math import ceil

video_card_price = int(input())
transition_price = int(input())
used_electricity_from_card = float(input())
profit_from_card = float(input())

total_spending = video_card_price * 13 + transition_price * 13 + 1000
total_profit_a_card = profit_from_card - used_electricity_from_card
total_profit_all_cards = total_profit_a_card * 13
days_for_return = ceil(total_spending / total_profit_all_cards)

print(total_spending)
print(days_for_return)


