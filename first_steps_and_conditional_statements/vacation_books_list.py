pages = int(input())
pages_for_one_hour = int(input())
total_days = int(input())

total_time_needed = pages // pages_for_one_hour
pages_a_day = total_time_needed // total_days

print(pages_a_day)