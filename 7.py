TOTAL_DISK_SPACE = 70000000
REQUIRED_SPACE = 30000000

class Node:
    def __init__(self, name: str, size: int, parent):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = size
        self.is_file = size > 0
    def __str__(self) -> str:
        return self.name

# Teil 1
def get_root():
    root_dir = Node("/",0, None)
    current_dir = root_dir
    with open("7.in","r") as file:        
        for line in [line.strip() for line in file.readlines()]:
            if line.startswith("$ ls"): continue
            if line.startswith("$ cd"):
                directory_name = line.split(" ")[2].strip()
                if directory_name == "..":
                    current_dir = current_dir.parent
                elif directory_name != "/":
                    current_dir = next(child for child in current_dir.children if child.name == directory_name)
            else:
                # ls content
                content = line.split(" ")
                if content[0].strip() == "dir":
                    current_dir.children.append(Node(content[1].strip(),0,current_dir))
                else:
                    current_dir.children.append(Node(content[1].strip(), int(content[0].strip()), current_dir))
    return root_dir

def print_tree(dir, indent):
    print(indent,"dir",dir.name)
    for child in dir.children:
        if child.is_file:
            print(indent+"  ", child.size, child.name)
        else:
            print_tree(child,indent+"  ")

def get_recursive_size(dir, sum=0) -> int:
    for child in dir.children:
        if child.is_file:
            sum += child.size
        else:
            sum += get_recursive_size(child)
    return sum

def get_all_dirs(dir) -> list[Node]:
    list = []
    for child in dir.children:
        if not child.is_file:
            list.append(child)
            list = list + get_all_dirs(child)
    return list


if __name__ == "__main__":
    # Teil 1
    sum = sum(get_recursive_size(dir) for dir in get_all_dirs(get_root()) if get_recursive_size(dir) < 100000)
    print("Answer Part 1:",sum)

    # Teil 2
    available_disk_space = TOTAL_DISK_SPACE - get_recursive_size(get_root())
    still_required_space = REQUIRED_SPACE - available_disk_space
    all_dirs_with_enough_size = [dir for dir in get_all_dirs(get_root()) if get_recursive_size(dir) > still_required_space]
    dir_to_delete = sorted(all_dirs_with_enough_size,key=lambda a: get_recursive_size(a))[0]
    print("Answer Part 2:", get_recursive_size(dir_to_delete))



