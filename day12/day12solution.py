class Node:
    def __init__(self, parent=None, position=None) -> None:
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    
    def __eq__(self, other) -> bool:
        return self.position == other.position


def astar(graph, start, end):
    open_list = []
    closed_list = []

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0

    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list.append(start_node)


    while len(open_list) > 0:
        current_node = open_list[0]
        current_node_index = 0

        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_node_index = index

        open_list.pop(current_node_index)
        closed_list.append(current_node)


        if current_node == end_node:
            path = []
            current = current_node

            while current is not None:
                path.append(current.position)
                current = current.parent

            return path[::-1]

        
        children = []

        for adjacent_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + adjacent_position[0], current_node.position[1] + adjacent_position[1])

            if node_position[1] > (len(graph) - 1) or node_position[1] < 0 or node_position[0] > (len(graph[len(graph) - 1]) - 1) or node_position[0] < 0:
                continue



            if (graph[current_node.position[1]][current_node.position[0]]) < ((graph[node_position[1]][node_position[0]])-1):
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)


        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            if child in open_list and child.g > start_node.g:
                continue

            open_list.append(child)


def parse_input():
    with open('./day12/input.txt', 'r') as file:
        lines = file.read().split('\n')

        graph = []
        start_node, end_node = None, None

        for y, line in enumerate(lines):
            current_row = []

            for x, char in enumerate(line):
                if char == 'S':
                    start_node = (x, y)
                    current_row.append(ord('a'))
                elif char == 'E':
                    end_node = (x, y)
                    current_row.append(ord('z'))
                else:
                    current_row.append(ord(char))

            graph.append(current_row)



        return graph, start_node, end_node

    
def main():
    graph, start_node, end_node = parse_input()


    path = astar(graph, start_node, end_node)

    print(len(path)-1)

if __name__ == '__main__':
    main()
        
