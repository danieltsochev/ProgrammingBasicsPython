won_matches = 0
lost_matches = 0
matches_count = 0

while True:
    name_of_tournament = input()

    if name_of_tournament == "End of tournaments":
        print(f"{(won_matches / matches_count) * 100}% matches win")
        print(f"{(lost_matches / matches_count) * 100}% matches lost")
        break

    games = int(input())
    game_counter = 0

    for _ in range(games):
        desi_sco = int(input())
        other_score = int(input())

        game_counter += 1
        matches_count += 1
        if desi_sco > other_score:
            won_matches += 1
            print(f"Game {game_counter} of tournament {name_of_tournament} win with {desi_sco - other_score} points.")

        elif other_score > desi_sco:
            lost_matches += 1
            print(f"Game {game_counter} of tournaments {name_of_tournament} lost with {other_score - desi_sco} points.")