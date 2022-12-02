score = 0

score_list = {
    'A': 1,
    'B': 2,
    'C': 3
}

mine_to_his = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

loser_winner = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

with open('a.txt', 'r') as file:
    for line in file.readlines():
        line = line.replace('\n', '')
        [his, mine] = line.split(' ')
        mine = mine_to_his[mine]
        score += score_list[mine]
        if loser_winner[his] == mine:
            score += 6
        elif loser_winner[mine] == his:
            score += 0
        else:
            score += 3
print(score)
