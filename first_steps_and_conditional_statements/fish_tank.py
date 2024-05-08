length, width, height = int(input()), int(input()), int(input())
percent_filled = float(input()) / 100

volume = length * width * height / 1000
volume -= volume * percent_filled

print(volume)