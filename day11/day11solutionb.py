from math import lcm


with open('./day11/input.txt', 'r') as file:
    commands = file.read().split('\n\n')
    monkeys = {}
    divisors = []

    for command in commands:
        command = command.split('\n')

        monkeys.update({command[0][-2:-1]: [command[1].split(' ')[4:], command[2].split(' ')[-2:], command[3].split(' ')[-1:][0], command[4][-1:], command[5][-1:], 0]})
        divisors.append(int(command[3].split(' ')[-1:][0]))


    base = lcm(*divisors)

    for i in range(10000):
        for monkey in monkeys.values():
            for _ in range(len(monkey[0])):
                monkey[5] += 1

                match monkey[1][0]:
                    case '*':
                        monkey[0][0] = (int(monkey[0][0]) * (int(monkey[1][1]) if monkey[1][1] != 'old' else int(monkey[0][0]))) % base
                    case '+':
                        monkey[0][0] = (int(monkey[0][0]) + (int(monkey[1][1]) if monkey[1][1] != 'old' else int(monkey[0][0]))) % base
                    case '-':
                        monkey[0][0] = (int(monkey[0][0]) - (int(monkey[1][1]) if monkey[1][1] != 'old' else int(monkey[0][0]))) % base

                if monkey[0][0] % int(monkey[2]) == 0:
                    monkeys.get(monkey[3])[0].append(monkey[0].pop(0))
                    
                else:
                    monkeys.get(monkey[4])[0].append(monkey[0].pop(0))



    print(sorted([monkey[5] for monkey in monkeys.values()])[-1] * sorted([monkey[5] for monkey in monkeys.values()])[-2])