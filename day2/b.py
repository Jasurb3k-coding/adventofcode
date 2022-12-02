score = 0

score_list = {
    'A': 1,
    'B': 2,
    'C': 3
}

loser_winner = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

winner_loser = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

with open('a.txt', 'r') as file:
    for line in file.readlines():
        line = line.replace('\n', '')
        [his, result] = line.split(' ')
        if result == 'X':
            mine = winner_loser[his]
        elif result == 'Z':
            mine = loser_winner[his]
            score += 6
        else:
            score += 3
            mine = his
        score += score_list[mine]
print(score)
