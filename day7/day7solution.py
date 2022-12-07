class Directory:
    sum_t = 0
    space_needed_for_update_v = 3956976
    current_smallest = 70000000

    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.child_directories = {}
        self.files = []

    #write repr method to print out the directory structure in a tree format (see example below) 
    # def __repr__(self) -> str:

    def __repr__(self) -> str:
        return f"{self.name}"
    

    def calculate_file_size(self) -> int:
        return sum(self.files)

    def calculate_directory_size(self) -> int:
        return sum([directory.get_size() for directory in self.child_directories.values()])
    
    def get_size(self) -> int:
        return self.calculate_file_size() + self.calculate_directory_size()

    def add_child_directory(self, directory) -> None:
        self.child_directories.update({directory.name: directory})

    def is_less_than_100000(self) -> int:
        for directory in self.child_directories.values():
            if directory.get_size() < 100000:
                Directory.sum_t += directory.get_size()

            directory.is_less_than_100000()
    
    def space_needed_for_update(self, root_dir_size) -> int:
        Directory.space_needed_for_update_v = 30000000 - (70000000 - root_dir_size)

    def delete_smallest_space_for_update(self) -> None:
        for directory in self.child_directories.values():
            if directory.get_size() >= Directory.space_needed_for_update_v:
                if directory.get_size() < Directory.current_smallest:
                    Directory.current_smallest = directory.get_size()

                
            directory.delete_smallest_space_for_update()



with open('./day7/input.txt', 'r') as file:
    commands = file.readlines()

    root_directory = Directory('/', None)
    current_directory = root_directory

    for count, command in enumerate(commands):
        command = command.split()

        if command[0] == "$":
            match command[1]:
                case "cd":
                    _, prefix, suffix = command

                    match suffix:
                        case "..":
                            current_directory = current_directory.parent
                        case "/":
                            current_directory = root_directory
                        case other:
                            current_directory = current_directory.child_directories.get(suffix)
        else:
            if command[0] == 'dir':
                new_dir = Directory(command[1], parent=current_directory)

                current_directory.add_child_directory(new_dir)
            else:
                current_directory.files.append(int(command[0]))

    
    root_directory.is_less_than_100000()

    print(Directory.sum_t)

    root_directory.space_needed_for_update(root_directory.get_size())
    root_directory.delete_smallest_space_for_update()
    print(Directory.current_smallest)
    
