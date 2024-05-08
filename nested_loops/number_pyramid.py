num = int(input())
counter = 0

for row in range(1, num + 1):
    for cow in range(1, row + 1):
        counter += 1
        print(counter, end=" ") if row != cow else print(counter)
        if counter == num:
            exit()