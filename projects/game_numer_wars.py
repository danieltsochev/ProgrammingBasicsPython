name1 = input()
name2 = input()

points1 = 0
points2 = 0

while True:
    c1_text = input()

    if c1_text == "End of game":
        print(f"{name1} has {points1} points")
        print(f"{name2} has {points2} points")
        break

    c2_text = input()

    c1 = int(c1_text)
    c2 = int(c2_text)

    if c1 > c2:
        points1 += (c1 - c2)
    elif c2 > c1:
        points2 += (c2 - c1)

    if c1 == c2:
        print("Number wars!")
        last1 = int(input())
        last2 = int(input())

        if last1 > last2:
            print(f"{name1} is winner with {points1} points")
            exit()

        elif last2 > last1:
            print(f"{name2} is winner with {points2} points")
            exit()
