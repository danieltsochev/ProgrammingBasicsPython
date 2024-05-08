numbers_of_floors = int(input())
flats_per_floor = int(input())

flat_name = ""
flat_number = 0

for current_floor in range(numbers_of_floors, 0, - 1):
    for number in range(flats_per_floor):
        apartment_number = current_floor * 10 + number
        if current_floor == numbers_of_floors:
            flat_name = f"L{apartment_number}"
        elif current_floor % 2 == 0:
            flat_name = f"O{apartment_number}"
        elif current_floor % 2 != 0:
            flat_name = f"A{apartment_number}"

        print(flat_name, end=" ")
    print()