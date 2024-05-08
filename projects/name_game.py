winner_name = ""
winner_points = 0
while True:
    player_name = input()
    if player_name == "Stop":
        break

    points = 0
    for i in range(len(player_name)):
        number = int(input())
        if chr(number) == player_name[i]:
            points += 10
        else:
            points += 2

    if points > winner_points:
        winner_name = player_name
        winner_points = points
    elif points == winner_points and len(player_name) < len(winner_name):
        winner_name = player_name
        winner_points = points

print(f"The winner is {winner_name} with {winner_points} points!")
