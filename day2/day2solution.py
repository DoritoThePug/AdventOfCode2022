scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

stratergy = {
    ('A', 'Y'): 6,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('A', 'X'): 3,
    ('B', 'Y'): 3,
    ('C', 'Z'): 3,
}

with open('./day2/input.txt', 'r') as file:
    games = [tuple(line.rstrip().split()) for line in file.readlines()]
    
    total_score = 0

    for game in games:
        total_score += stratergy.get(game, 0) + scores.get(game[1])

    print(total_score)