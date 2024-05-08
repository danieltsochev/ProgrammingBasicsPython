students_count = int(input())

fail = 0
between_3_4 = 0
between_4_5 = 0
top = 0
counter = 0

for _ in range(students_count):
    student_score = float(input())
    counter += student_score

    if 2.00 <= student_score <= 2.99:
        fail += 1
        fail_percent = fail / students_count * 100

    elif 3.00 <= student_score <= 3.99:
        between_3_4 += 1
        between_percent_3_4 = between_3_4 / students_count * 100

    elif 4.00 <= student_score <= 4.99:
        between_4_5 += 1
        between_percent_4_5 = between_4_5 / students_count * 100

    elif student_score >= 5:
        top += 1
        top_percent = top / students_count * 100


print(f"Top students: {top_percent:.2f}%")
print(f"Between 4.00 and 4.99: {between_percent_4_5:.2f}%")
print(f"Between 3.00 and 3.99: {between_percent_3_4:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {counter / students_count:.2f}")
