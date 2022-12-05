with open('./day4/input.txt', 'r') as file:
    assignments = file.readlines()

    sum = 0

    for assignment in assignments:
        assignment1, assignment2 = assignment.split(',')
        assignment1 = list(map(int, assignment1.split('-')))
        assignment2 = list(map(int, assignment2.split('-')))
        
        if assignment1[0] <= assignment2[0] and assignment1[1] >= assignment2[1]:
            sum += 1
        elif assignment2[0] <= assignment1[0] and assignment2[1] >= assignment1[1]:
            sum += 1

    print(sum)