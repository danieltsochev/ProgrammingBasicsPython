from math import floor

cat_breed = input()
cat_gender = input()
cat_life = 0

if cat_breed == "British Shorthair":
    if cat_gender == "m":
        cat_life = floor((13 * 12) / 6)
    elif cat_gender == "f":
        cat_life = floor((14 * 12) / 6)

elif cat_breed == "Siamese":
    if cat_gender == "m":
        cat_life = floor((15 * 12) / 6)
    elif cat_gender == "f":
        cat_life = floor((16 * 12) / 6)

elif cat_breed == "Persian":
    if cat_gender == "m":
        cat_life = floor((14 * 12) / 6)
    elif cat_gender == "f":
        cat_life = floor((15 * 12) / 6)

elif cat_breed == "Ragdoll":
    if cat_gender == "m":
        cat_life = floor((16 * 12) / 6)
    elif cat_gender == "f":
        cat_life = floor((17 * 12) / 6)

elif cat_breed == "American Shorthair":
    if cat_gender == "m":
        cat_life = floor((12 * 12) / 6)
    elif cat_gender == "f":
        cat_life = floor((13 * 12) / 6)

elif cat_breed == "Siberian":
    if cat_gender == "m":
        cat_life = floor((11 * 12) / 6)
    elif cat_gender == "f":
        cat_life = floor((12 * 12) / 6)

else:
    print(f"{cat_breed} is invalid cat!")
    exit()

print(f"{cat_life} cat months")





