import string

ALPHABET = string.ascii_letters

with open('./day3/input.txt', 'r') as file:
    sum = 0

    for rucksac in file.readlines():
        rucksac = rucksac.rstrip()

        compartment1, compartment2 = rucksac[:(len(rucksac)//2)], rucksac[len(rucksac)//2:]
        
        # for item in compartment1:
        #     if item in compartment2:
        #         sum += ALPHABETE.index(item)+1
        #         break

        sum += ALPHABET.index(list(set(compartment1).intersection(compartment2))[0]) + 1

    print(sum)
