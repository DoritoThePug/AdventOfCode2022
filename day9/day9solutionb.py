# def is_touching(pos_x,h_pos):
#     if pos_x == h_pos: # if the coordinates are the same
#         return True
#     elif pos_x[0] == h_pos[0] and (h_pos[1]+1) >= pos_x[1] >= (h_pos[1]-1): # if the x coordinates are the same and the y coordinates are within 1 of each other
#         return True
#     elif pos_x[1] == h_pos[1] and (h_pos[0]+1) >= pos_x[0] >= (h_pos[0]-1): # if the y coordinates are the same and the x coordinates are within 1 of each other
#         return True
#     elif pos_x[1] == (h_pos[1] + 1) and (h_pos[0] + 1) >= pos_x[0] >= (h_pos[0] - 1): # if the y coordinates are 1 greater than the other and the x coordinates are within 1 of each other
#         return True
#     elif pos_x[1] == (h_pos[1] - 1) and (h_pos[0] + 1) >= pos_x[0] >= (h_pos[0] - 1): # if the y coordinates are 1 less than the other and the x coordinates are within 1 of each other
#         return True
#     else:
#         return False


# # print(is_touching((1,4),(3,4)))

# def find_shortest_route(pos_x, h_pos): # return (x, y) for t_pos
#     if not is_touching(pos_x, h_pos):
#         if pos_x[0] == h_pos[0]:
#             if pos_x[1] > h_pos[1]:
#                 return (pos_x[0], pos_x[1] - 1)
#             else:
#                 return (pos_x[0], pos_x[1] + 1)
#         elif pos_x[1] == h_pos[1]:
#             if pos_x[0] > h_pos[0]:
#                 return (pos_x[0] - 1, pos_x[1])
#             else:
#                 return (pos_x[0] + 1, pos_x[1])
#         elif pos_x[1] > h_pos[1]:
#             if pos_x[0] > h_pos[0]:
#                 return (pos_x[0] - 1, pos_x[1] - 1)
#             else:
#                 return (pos_x[0] + 1, pos_x[1] - 1)
#         elif pos_x[1] < h_pos[1]:
#             if pos_x[0] > h_pos[0]:
#                 return (pos_x[0] - 1, pos_x[1] + 1)
#             else:
#                 return (pos_x[0] + 1, pos_x[1] + 1)

# # print(find_shortest_route((3,4),(1,4)))

# with open('./day9/input.txt', 'r')  as file:
#     commands = file.read().splitlines()

#     knots = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)] # coordinates (x, y)

#     visited_coords = []

#     visited_coords.append((0,0))

#     for command in commands:
#         direction, amount = command.split()


#         for i in range(int(amount)):
#             match direction:
#                 case 'U':
#                     knots[0] = (knots[0][0], knots[0][1] + 1)
#                 case 'D':
#                     knots[0] = (knots[0][0], knots[0][1] - 1)
#                 case 'L':
#                     knots[0] = (knots[0][0] - 1, knots[0][1])
#                 case 'R':
#                     knots[0] = (knots[0][0] + 1, knots[0][1])


#             if is_touching(knots[1], knots[0]):
#                 pass
#             else:
#                 for count, knot in enumerate(knots):
#                     if count == 0:
#                         continue

#                     if is_touching(knots[count-1], knot):
#                         continue
#                     else:
#                         knots[count-1] = find_shortest_route(knots[count-1], knot)

#             #     print(knots)
#             #     visited_coords.append(knots[9])

#             print(knots)

            

#             # print(h_pos, t_pos)

#     # print(len(set(visited_coords)))

        



    


def is_touching(t_pos, h_pos):
    if t_pos == h_pos: # if the coordinates are the same
        return True
    elif t_pos[0] == h_pos[0] and (h_pos[1]+1) >= t_pos[1] >= (h_pos[1]-1): # if the x coordinates are the same and the y coordinates are within 1 of each other
        return True
    elif t_pos[1] == h_pos[1] and (h_pos[0]+1) >= t_pos[0] >= (h_pos[0]-1): # if the y coordinates are the same and the x coordinates are within 1 of each other
        return True
    elif t_pos[1] == (h_pos[1] + 1) and (h_pos[0] + 1) >= t_pos[0] >= (h_pos[0] - 1): # if the y coordinates are 1 greater than the other and the x coordinates are within 1 of each other
        return True
    elif t_pos[1] == (h_pos[1] - 1) and (h_pos[0] + 1) >= t_pos[0] >= (h_pos[0] - 1): # if the y coordinates are 1 less than the other and the x coordinates are within 1 of each other
        return True
    else:
        return False


# print(is_touching((1,4),(3,4)))

def find_shortest_route(t_pos, h_pos): # return (x, y) for t_pos
    if not is_touching(t_pos, h_pos):
        if t_pos[0] == h_pos[0]:
            if t_pos[1] > h_pos[1]:
                return (t_pos[0], t_pos[1] - 1)
            else:
                return (t_pos[0], t_pos[1] + 1)
        elif t_pos[1] == h_pos[1]:
            if t_pos[0] > h_pos[0]:
                return (t_pos[0] - 1, t_pos[1])
            else:
                return (t_pos[0] + 1, t_pos[1])
        elif t_pos[1] > h_pos[1]:
            if t_pos[0] > h_pos[0]:
                return (t_pos[0] - 1, t_pos[1] - 1)
            else:
                return (t_pos[0] + 1, t_pos[1] - 1)
        elif t_pos[1] < h_pos[1]:
            if t_pos[0] > h_pos[0]:
                return (t_pos[0] - 1, t_pos[1] + 1)
            else:
                return (t_pos[0] + 1, t_pos[1] + 1)

# print(find_shortest_route((3,4),(1,4)))

with open('./day9/input.txt', 'r')  as file:
    commands = file.read().splitlines()

    knots = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)] # coordinates (x, y)

    visited_coords = []

    visited_coords.append((0,0))

    for command in commands:
        direction, amount = command.split()


        for i in range(int(amount)):
            match direction:
                case 'U':
                    knots[0] = (knots[0][0], knots[0][1] + 1)
                case 'D':
                    knots[0] = (knots[0][0], knots[0][1] - 1)
                case 'L':
                    knots[0] = (knots[0][0] - 1, knots[0][1])
                case 'R':
                    knots[0] = (knots[0][0] + 1, knots[0][1])

            if is_touching(knots[1], knots[0]):
                pass
            else:
                for count, knot in enumerate(knots):
                    if count <= 8:
                        if is_touching(knots[count+1], knot):
                            break
                        else:
                            knots[count+1] = find_shortest_route(knots[count+1], knot)


                visited_coords.append(knots[9])


            # print(h_pos, t_pos)

    print(len(set(visited_coords)))

        



    
