capacity = float(input())

loaded_bags = 0
suitcases_counter = 0

command = input()

while command != "End":

    suitcase = float(command)

    if suitcases_counter % 3 == 0 and suitcases_counter > 0:
        suitcase *= 1.10

    if capacity >= suitcase:
        capacity -= suitcase
        loaded_bags += 1
        suitcases_counter += 1

    else:
        print("No more space!")
        break

    command = input()

if command == "End":
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcases_counter} suitcases loaded.")












