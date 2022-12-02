scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3
}

stratergy = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
    
}

start_1 = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

with open('./day2/input.txt', 'r') as file:
    games = [tuple(line.rstrip().split()) for line in file.readlines()]
    
    total_score = 0

    for game in games:
        if game[1] == 'Y':
            total_score += scores.get(game[0]) + 3
        elif game[1] == 'X':
            total_score += scores.get(start_1.get(game[0]))
        else:
            total_score += scores.get(stratergy.get(game[0])) + 6
        

    print(total_score)