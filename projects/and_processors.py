from math import floor

processors_count = int(input())
staff_count = int(input())
working_days = int(input())

production_time = staff_count * working_days * 8

production_processors = floor(production_time / 3)

if production_processors >= processors_count:
    print(f"Profit: -> {(production_processors - processors_count) * 110.10:.2f} BGN")
else:
    print(f"Losses: -> {(processors_count - production_processors) * 110.10:.2f} BGN")
