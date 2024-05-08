from math import floor

processors_amount_needed = int(input())
workers_count = int(input())
working_days = int(input())

PROCESSOR_PRICE = 110.10

total_working_hours = (workers_count * working_days) * 8
processors_done = floor(total_working_hours / 3)

if processors_done >= processors_amount_needed:
    print(f"Profit: -> {abs(processors_done - processors_amount_needed) * PROCESSOR_PRICE:.2f} BGN")

else:
    print(f"Losses: -> {abs(processors_amount_needed - processors_done) * PROCESSOR_PRICE:.2f} BGN")