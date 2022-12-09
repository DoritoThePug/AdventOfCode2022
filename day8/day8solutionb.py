import numpy as np

def find_first_tree_big(array, current_tree):
    for count, tree in enumerate(array):
        if tree >= current_tree:
            return count+1

    return array.size
            

with open('./day8/input.txt', 'r') as file:
    trees = file.readlines()

    best_scenic_score = 0
    f, e = 0, 0

    tree_grid = np.array([list(tree.rstrip()) for tree in trees], dtype=int)

    x_size, y_size = tree_grid.shape


    for y in range(0, y_size):
        for x in range(0, x_size):
            current_tree = tree_grid[y][x]

            left, right, top, bottom = find_first_tree_big(np.flip(tree_grid[y][0:x]), current_tree), find_first_tree_big(tree_grid[y][x+1:x_size+1], current_tree), find_first_tree_big(np.flip(tree_grid[0:y, x]), current_tree), find_first_tree_big(tree_grid[y+1:x_size, x], current_tree)

            if top*bottom*left*right > best_scenic_score:
                best_scenic_score = top*bottom*left*right
                print(top, left, right, bottom, x, y, current_tree)

    print(best_scenic_score)