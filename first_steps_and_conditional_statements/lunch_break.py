from math import ceil

series_name = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
leisure_time = break_length / 4

time_taken = lunch_time + leisure_time + episode_length
time_left = break_length - time_taken

if time_left >= 0:
    print(f"You have enough time to watch {series_name} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(abs(time_left))} more minutes.")