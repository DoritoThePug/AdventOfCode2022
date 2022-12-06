with open('./day5/input.txt') as file:
    lines = file.readlines()

    crates = [
        ['F', 'T', 'N', 'Z','M','G','H','J'],
        ['J', 'W', 'V'],
        ['H', 'T', 'B', 'J', 'L', 'V', 'G'],
        ['L', 'V', 'D', 'C', 'N', 'J', 'P', 'B'],
        ['G', 'R', 'P', 'M', 'S', 'W', 'F'],
        ['M', 'V', 'N', 'B', 'F', 'C', 'H', 'G'],
        ['R', 'M', 'G', 'H', 'D'],
        ['D', 'Z', 'V', 'M', 'N', 'H'],
        ['H', 'F', 'N', 'G']
    ]

    crates2 = [
        ['F', 'T', 'N', 'Z','M','G','H','J'],
        ['J', 'W', 'V'],
        ['H', 'T', 'B', 'J', 'L', 'V', 'G'],
        ['L', 'V', 'D', 'C', 'N', 'J', 'P', 'B'],
        ['G', 'R', 'P', 'M', 'S', 'W', 'F'],
        ['M', 'V', 'N', 'B', 'F', 'C', 'H', 'G'],
        ['R', 'M', 'G', 'H', 'D'],
        ['D', 'Z', 'V', 'M', 'N', 'H'],
        ['H', 'F', 'N', 'G']
    ]

    for line in lines:
        _, amount, _, origin, _, destination = line.split(' ')


        crates[int(destination)-1] = crates[int(origin)-1][int(amount)-1::-1] + crates[int(destination)-1]
        crates[int(origin)-1] = crates[int(origin)-1][int(amount):] 

        crates2[int(destination)-1] = crates2[int(origin)-1][:int(amount)] + crates2[int(destination)-1]
        crates2[int(origin)-1] = crates2[int(origin)-1][int(amount):] 

        

    print(f"Part 1: {''.join([crate[0] for crate in crates])}")
    print(f"Part 2: {''.join([crate[0] for crate in crates2])}")



            
        