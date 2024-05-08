days_counter = 1
meters_reached = 5364

while True:
    command = input()
    if command == "END":
        break
    elif command == "Yes":
        days_counter += 1

    current_meters = int(input())
    meters_reached += current_meters

    if days_counter > 5:
        break

    if meters_reached >= 8848:
        break

if meters_reached >= 8848:
    print(f"Goal reached for {days_counter} days!")
else:
    print("Failed!")
    print(meters_reached)









