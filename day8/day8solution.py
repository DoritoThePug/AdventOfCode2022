import numpy as np

with open('./day8/input.txt', 'r') as file:
    trees = file.readlines()

    tree_grid = []
    visible_trees = 0

    tree_grid = np.array([list(tree.rstrip()) for tree in trees], dtype=int)


    x_size, y_size = tree_grid.shape

    for y in range(1, y_size-1):
        for x in range(1, x_size-1):
            current_tree = tree_grid[y][x]

            if max(tree_grid[y][0:x]) < current_tree or \
            max(tree_grid[y][x+1:x_size+1]) < current_tree or \
            max(tree_grid[0:y, x]) < current_tree or \
            max(tree_grid[y+1:x_size, x]) < current_tree:
                visible_trees += 1
                print(x, y, current_tree)

    visible_trees += (tree_grid.shape[0] * 2) + ((tree_grid.shape[1]-2) * 2)

    print(visible_trees)
    