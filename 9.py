import numpy as np

def get_pos_amount_of_tail(filename, knot_amount:int = 2) -> int:
    op_code = {"L":(-1,0),"R":(1,0),"U":(0,1),"D":(0,-1)}
    visited_positions = []
    knot_positions = []
    for _ in range(knot_amount):
        knot_positions.append((0,0))
    visited_positions.append(knot_positions[-1])

    with open(filename,"r") as file:
        for line in [line.strip() for line in file.readlines()]:
            operation = line.split(" ")[0]
            amount = int(line.split(" ")[1])
            
            # every step
            for _ in range(amount):
                knot_positions[0] = tuple(np.add(knot_positions[0], op_code[operation]))
                for i in range(1,len(knot_positions)):
                    offset = tuple(np.subtract(knot_positions[i-1],knot_positions[i]))
                    distance = np.linalg.norm(np.array(knot_positions[i-1]) - np.array(knot_positions[i]))
                    if distance > np.sqrt(2):
                        divisorX = abs(offset[0]) if abs(offset[0]) != 0 else 1
                        divisorY = abs(offset[1]) if abs(offset[1]) != 0 else 1
                        knot_positions[i] = tuple(np.add(knot_positions[i], (offset[0]//divisorX,offset[1]//divisorY)))
                if knot_positions[-1] not in visited_positions:
                    visited_positions.append(knot_positions[-1])
    return len(visited_positions)


if __name__ == "__main__":
    print("Part 1:", get_pos_amount_of_tail("9.in", knot_amount=2))
    print("Part 2:", get_pos_amount_of_tail("9.in", knot_amount=10))