with open('./day6/input.txt', 'r') as file:
    buffer = list(file.read())


    for count, char in enumerate(buffer):
        cbuffer = buffer[count:count+4]

        if len(set(cbuffer)) == len(cbuffer):
            print("Part 1: ", count+4)
            break

    for count, char in enumerate(buffer):
        cbuffer = buffer[count:count+14]

        if len(set(cbuffer)) == len(cbuffer):
            print("Part 2: ", count+14)
            break