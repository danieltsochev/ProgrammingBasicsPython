best_movie = ''
best_score = float('-inf')
limit_reached = False

while not limit_reached:
    title = input()
    if title == 'STOP':
        break
    score = sum(ord(char) for char in title)
    length = len(title)
    for char in title:
        if char.islower():
            score -= 2 * length
        elif char.isupper():
            score -= length
    if score > best_score:
        best_movie = title
        best_score = score

    if best_movie and title != best_movie and len(title) >= len(best_movie):
        limit_reached = True
        print('The limit is reached.')
        break

print(f'The best movie for you is {best_movie} with {best_score} ASCII sum.')
