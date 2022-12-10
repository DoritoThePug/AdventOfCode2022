from numpy import prod

with open('./day10/input.txt', 'r') as file:
    instructions = file.readlines()

    command_sequence = []

    current_cycle = 1

    x = 1

    signal_strengths = []

    for instruction in instructions:
        print(instruction, current_cycle)

        match instruction.rstrip():
            case 'noop':
                if current_cycle == 20 or current_cycle == 60 or current_cycle == 100 or current_cycle == 140 or current_cycle == 180 or current_cycle == 220:
                    signal_strengths.append(x * current_cycle)
                    print(current_cycle, x)

                current_cycle += 1

            case other:
                _, amount = instruction.split()

                if current_cycle == 20 or current_cycle == 60 or current_cycle == 100 or current_cycle == 140 or current_cycle == 180 or current_cycle == 220:
                    signal_strengths.append(x * current_cycle)
                    print(current_cycle, x)

                current_cycle += 1

                if current_cycle == 20 or current_cycle == 60 or current_cycle == 100 or current_cycle == 140 or current_cycle == 180 or current_cycle == 220:
                    signal_strengths.append(x * current_cycle)
                


                current_cycle += 1

                x += int(amount)

        
                


    print(sum(signal_strengths))
    

        # command_sequence[0] = (command_sequence[0][0], command_sequence[0][1] - 1) 

        # if command_sequence[0][1] == 0:
        #     executing_command = command_sequence.pop(0)

        #     if executing_command[0] == 'noop':
        #         continue
        #     else:
        #         x += int(executing_command[0])
        #         print(x)

        # print(command_sequence)




