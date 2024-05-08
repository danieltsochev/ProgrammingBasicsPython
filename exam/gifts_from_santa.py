n = int(input())
m = int(input())
s = int(input())

for numbers in range(m, n, - 1):
    if numbers == s and numbers % 2 == 0 and numbers % 3 == 0:
        break
    elif numbers == s and numbers % 2 != 0 and numbers % 3 != 0:
        continue
    if numbers % 2 == 0 and numbers % 3 == 0:

        print(numbers, end=" ")






















