def get_sum_part1(filename):
    sum = 1
    product_sum = 0
    clock = 0
    with open(filename,"r") as file:
        for line in [line.strip() for line in file.readlines()]:
            clock += 1
            if is_mark(clock):
                product_sum += sum * clock
            if line.split(" ")[0] == "addx":
                clock += 1
                if is_mark(clock):
                    product_sum += sum * clock
                add_amount = int(line.split(" ")[1])
                sum += add_amount
    return product_sum
            
def part2(filename) -> str:
    print_string = ""
    sprite_pos = (0,1,2)
    clock = 0
    with open(filename,"r") as file:
        for line in [line.strip() for line in file.readlines()]:
            if clock in sprite_pos:
                print_string += "#"
            else:
                print_string += "."
            clock += 1
            if clock % 40 == 0:
                clock = 0
                print_string += "\n"
            if line.split(" ")[0] == "addx":
                if clock in sprite_pos:
                    print_string += "#"
                else:
                    print_string += "."
                clock += 1
                if clock % 40 == 0:
                    clock = 0
                    print_string += "\n"
                add_amount = int(line.split(" ")[1])
                sprite_pos = (sprite_pos[0] + add_amount, sprite_pos[1] + add_amount, sprite_pos[2] + add_amount)
                
    return "\n"+print_string
                


def is_mark(clock) -> bool:
    return clock == 20 or clock == 60 or clock == 100 or clock == 140 or clock == 180 or clock == 220
        

if __name__ == "__main__":
    print("Part 1:",get_sum_part1("10.in"))
    print("Part 2:",part2("10.in"))