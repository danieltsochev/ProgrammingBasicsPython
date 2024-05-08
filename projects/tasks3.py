name_of_player = input()

start_points = 301

yes_shot_counter = 0
no_shot_counter = 0

while start_points != 0:

    shot_type = input()

    if shot_type == "Retire":
        print(f"{name_of_player} retired after {no_shot_counter} unsuccessful shots.")
        break

    points = int(input())

    if shot_type == "Single":
        start_points -= points
        if start_points >= points:
            yes_shot_counter += 1
        else:
            no_shot_counter += 1

    elif shot_type == "Double":
        start_points -= points * 2
        if start_points >= points:
            yes_shot_counter += 1
        else:
            no_shot_counter += 1

    elif shot_type == "Triple":
        start_points -= points * 3
        if start_points >= points:
            yes_shot_counter += 1
        else:
            no_shot_counter += 1

    if start_points == 0:
        print(f"{name_of_player} won the leg with {yes_shot_counter} shots.")

















