from functools import cmp_to_key
from math import prod

def find_sum(filename) -> int:
    right_order_indices = []
    cur_index = 1
    with open(filename,"r") as file:
        for block in [block.strip() for block in file.read().strip().split("\n\n")]:
            comp1 = eval(block.split("\n")[0])
            comp2 = eval(block.split("\n")[1])
            if cmp(comp1,comp2) == -1:
                right_order_indices.append(cur_index)
            cur_index += 1
            # break
    return sum(right_order_indices)

def sort_packets(filename):
    mark = [[[2]],[[6]]]
    with open(filename,"r") as file:
        packets = [eval(line.strip()) for line in file.readlines() if len(line.strip()) > 0]
        packets += mark
    return prod(i+1 for i,p in enumerate(sorted(packets, key=cmp_to_key(cmp))) if p in mark)
    
            

def cmp(comp1, comp2):
    match comp1, comp2:
        case int(), int():  return (comp1>comp2) - (comp1<comp2)
        case int(), list(): return cmp([comp1], comp2)
        case list(), int(): return cmp(comp1, [comp2])
        case list(), list():
            for z in map(cmp, comp1, comp2):
                if z: return z
            return cmp(len(comp1), len(comp2))

if __name__ == "__main__":
    print("Part1:",find_sum("13.in"))
    print("Part2:",sort_packets("13.in"))