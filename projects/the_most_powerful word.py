most_powerful_word = ""
most_powerful_word_score = 0

while True:
    word = input()
    if word == "End of words":
        break

    score = sum(ord(c) for c in word)
    if word[0].lower() in "aeiouy":
        score *= len(word)
    else:
        score = int(score / len(word))

    if score > most_powerful_word_score:
        most_powerful_word = word
        most_powerful_word_score = score

print(f"The most powerful word is {most_powerful_word} - {most_powerful_word_score}")
