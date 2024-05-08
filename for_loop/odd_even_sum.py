number_of_lines = int(input())

odd_sum = 0
even_sum = 0

for i in range(1, number_of_lines + 1):
    current_number = int(input())

    if i % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if even_sum == odd_sum:
    print(f"Yes\nSum = {even_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print(f"No\nDiff = {diff}")