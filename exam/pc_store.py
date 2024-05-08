processor_price = float(input())
video_card_price = float(input())
ram_memory_price = float(input())
ram_memory_count = int(input())
discount = float(input())

processor_price_lv = processor_price * 1.57
processor_price_lv_d = processor_price_lv - processor_price_lv * discount
video_card_price_lv = video_card_price * 1.57
video_card_price_lv_d = video_card_price_lv - video_card_price_lv * discount
ram_memory_price_lv = (ram_memory_price * ram_memory_count) * 1.57

total_price = processor_price_lv_d + video_card_price_lv_d + ram_memory_price_lv

print(f"Money needed - {total_price:.2f} leva.")