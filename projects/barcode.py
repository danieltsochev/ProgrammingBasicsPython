start = int(input())   # starting barcode number
end = int(input())     # ending barcode number

# loop through all possible barcode numbers within the given range
for i in range(start, end+1):
    # convert the current barcode number to a string for easy digit manipulation
    barcode_str = str(i)
    # assume the current barcode does not contain any even digits
    has_even_digit = False
    # loop through all digits of the current barcode
    for digit in barcode_str:
        # check if the current digit is even
        if int(digit) % 2 == 0:
            # if the current digit is even, set the flag and exit the loop
            has_even_digit = True
            break
    # if the current barcode does not contain any even digits, print it
    if not has_even_digit:
        print(i, end=" ")
