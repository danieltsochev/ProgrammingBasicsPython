won_games = 0
lost_game = 0
all_games = 0

while True:
    name_of_game = input()

    if name_of_game == "End of tournaments":
        break

    games_count = int(input())
    counter_games = 0

    for _ in range(games_count):
        desi_score = int(input())
        enemy_score = int(input())

        counter_games += 1
        all_games += 1

        if desi_score > enemy_score:
            won_games += 1
            print(f"Game {counter_games} of tournament {name_of_game}: win with {desi_score - enemy_score} points.")
        elif desi_score < enemy_score:
            lost_game += 1
            print(f"Game {counter_games} of tournament {name_of_game}: lost with {enemy_score - desi_score} points.")

print(f"{(won_games / all_games) * 100:.2f}% matches win")
print(f"{(lost_game / all_games) * 100:.2f}% matches lost")