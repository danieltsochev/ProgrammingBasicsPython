CONSTANT_NUMBER = int(input())

sum_numbers = 0

while True:
    current_number = int(input())
    sum_numbers += current_number

    if sum_numbers >= CONSTANT_NUMBER:
        print(sum_numbers)
        break
