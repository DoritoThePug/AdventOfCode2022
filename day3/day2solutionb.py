import string

ALPHABET = string.ascii_letters

with open('./day3/input.txt', 'r') as file:
    sum = 0
    
    lines = file.readlines()

    for i in range(0, len(lines), 3):
        elf1, elf2, elf3 = lines[i].rstrip(), lines[i+1].rstrip(), lines[i+2].rstrip()

        sum += ALPHABET.index(list(set(elf1).intersection(elf2).intersection(elf3))[0]) +1

    print(sum)
