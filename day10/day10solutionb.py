with open('./day10/input.txt', 'r') as file:
    instructions = file.readlines()

    screen = []

    row = []

    current_cycle = 1

    x = 1

    signal_strengths = []

    for instruction in instructions:
        print(current_cycle)

        match instruction.rstrip():
            case 'noop':
                if x <= current_cycle and x+2 >= current_cycle:
                    row.append("#")
                else:
                    row.append(".")


                current_cycle += 1

                if current_cycle == 41:
                    print(len(row))
                    screen.append(''.join(row))
                    row = []
                    current_cycle = 1 
            case other:
                _, amount = instruction.split()

                if x <= current_cycle and x+2 >= current_cycle:
                    row.append("#")
                else:
                    row.append(".")

                current_cycle += 1  
                
                if current_cycle == 41:
                    print(len(row))
                    screen.append(''.join(row))
                    row = []
                    current_cycle = 1    

                if x <= current_cycle and x+2 >= current_cycle:
                    row.append("#")
                else:
                    row.append(".")          

                x += int(amount)
                current_cycle += 1

                if current_cycle == 41:
                    print(len(row))
                    screen.append(''.join(row))
                    row = []
                    current_cycle = 1
                


    print(screen)




