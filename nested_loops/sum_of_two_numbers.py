start_interval_number = int(input())
final_interval_number = int(input())
magic_number = int(input())

combination_counter = 0
break_condition = False

for num1 in range(start_interval_number, final_interval_number + 1):
    for num2 in range(start_interval_number, final_interval_number + 1):
        combination_counter += 1

        if num1 + num2 == magic_number:
            break_condition = True
            print(f"Combination N:{combination_counter} ({num1} + {num2} = {magic_number})")
            break

    if break_condition:
        break

if not break_condition:
    print(f"{combination_counter} combinations - neither equals {magic_number}")