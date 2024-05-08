maiden_party_price = float(input())
love_message_count = int(input())
wax_rose_count = int(input())
keychain_count = int(input())
caricature_count = int(input())
lucky_surprise_count = int(input())

LOVE_MESSAGE_PRICE = 0.60
WAX_ROSE_PRICE = 7.20
KEYCHAIN_PRICE = 3.60
CARICATURE_PRICE = 18.20
LUCKY_SURPRISE_PRICE = 22

total_count = love_message_count + wax_rose_count + keychain_count + caricature_count + lucky_surprise_count
total_price_b_host = (love_message_count * LOVE_MESSAGE_PRICE) + (wax_rose_count * WAX_ROSE_PRICE) \
+ (keychain_count * KEYCHAIN_PRICE) + (caricature_count * CARICATURE_PRICE) + \
 (lucky_surprise_count * LUCKY_SURPRISE_PRICE)

if total_count >= 25:
    total_price_b_host *= 0.65
else:
    total_price_b_host *= 1

total_price = total_price_b_host * 0.90

if total_price >= maiden_party_price:
    print(f"Yes! {total_price - maiden_party_price:.2f} lv left.")
else:
    print(f"Not enough money! {maiden_party_price - total_price:.2f} lv needed.")