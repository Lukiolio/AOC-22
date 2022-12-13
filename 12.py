import string

def get_parsed_input(filename):
    with open(filename, "r") as file:
        height_map = [list(line.strip()) for line in file.readlines()]
        for row in range(len(height_map)):
            for column in range(len(height_map[row])):
                value = height_map[row][column]
                if value == 'S':
                    cur_pos = (row, column)
                    height_map[row][column] = 0
                elif value == 'E':
                    target_pos = (row,column)
                    height_map[row][column] = 25
                else:
                    height_map[row][column] = string.ascii_lowercase.index(value)
    return height_map, cur_pos, target_pos
    
def find_shortest_path(height_map, starting_pos, target_pos) -> int:
    R,C = len(height_map), len(height_map[0])
    visited = set()
    queue = [(*starting_pos,0)]
    while queue:
        cr,cc,v = queue.pop(0)
        if (cr,cc) in visited:
            continue
        visited.add((cr,cc))
        if (cr,cc) == target_pos:
            return v
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            rr = cr+dr
            rc = cc+dc
            if 0 <= rr < R and 0 <= rc < C and height_map[rr][rc] - 1 <= height_map[cr][cc]:
                queue.append((rr,rc, v+1))
        
    
def find_best_starting_point(height_map, _, target_pos) -> int:
    all_path_lengths = []
    for r in range(len(height_map)):
        for c in range(len(height_map[r])):
            if height_map[r][c] == 0:
                all_path_lengths.append(find_shortest_path(height_map,(r,c),target_pos))
    return min([e for e in all_path_lengths if e != None])

if __name__ == "__main__":
    print("Part1:",find_shortest_path(*get_parsed_input("12.in")))
    print("Part2:",find_best_starting_point(*get_parsed_input("12.in")))