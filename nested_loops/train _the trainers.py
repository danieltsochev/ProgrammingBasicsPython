judges = int(input())

total_grades = 0
total_grades_sum = 0

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        break

    grade_sum = 0

    for _ in range(judges):
        grade_sum += float(input())

    total_grades_sum += grade_sum
    total_grades += judges

    print(f"{presentation_name} - {grade_sum / judges:.2f}.")


print(f"Student's final assessment is {total_grades_sum / total_grades:.2f}.")
