from itertools import zip_longest

def test(first, second):
    for first_2, second_2 in zip_longest(first, second, fillvalue=-1):
        # print(first_2, second_2)
        if first_2 == second_2:
            continue
        elif second_2 == -1:
            return False
        elif first_2 == -1:
            return True
        elif isinstance(first_2, int) and isinstance(second_2, int):
            if first_2 > second_2:
                return False
            elif first_2 < second_2:
                return True
            else:
                continue
        elif isinstance(first_2, list) and isinstance(second_2, list):
            if test(first_2, second_2):
                return True
            else:
                return False
        elif isinstance(first_2, list) and isinstance(second_2, int):
            if test(first_2, [second_2]):
                return True
            else:
                return False
        elif isinstance(first_2, int) and isinstance(second_2, list):
            if test([first_2], second_2):
                return True
            else:
                return False


    return True


print(test([[2, 0]], [[2], [7]]))