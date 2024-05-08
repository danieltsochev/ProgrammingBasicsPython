period_days = int(input())

treated = 0
untreated = 0
treated_possible = 7

for day in range(1, period_days + 1):
    patients = int(input())

    if patients <= treated_possible:
        treated += patients
    elif patients > treated_possible:
        treated += treated_possible
        untreated += (patients - treated_possible)

    if day % 3 == 0 and untreated > treated:
        treated_possible += 1
        treated += 1
        untreated -= 1


print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")

