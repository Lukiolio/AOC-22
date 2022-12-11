class Monkey:
    def __init__(self, monkey_block):
        self.inspection_count = 0
        self.monkey_num = int(monkey_block[0][7])
        self.starting_items = [int(item) for item in monkey_block[1].split(": ")[1].split(", ")]
        self.operation_str = monkey_block[2].split("old ")[1] if "old" not in monkey_block[2].split("old ")[1] else "** 2"
        self.divisor = int(monkey_block[3].split("by ")[1])
        self.target1 = int(monkey_block[4].split("monkey ")[1])
        self.target2 = int(monkey_block[5].split("monkey ")[1])

    def __str__(self) -> str:
        return f"{self.monkey_num}:{self.inspection_count}x"

def part1(filename, round_amount = 20) -> int:
    with open(filename,"r") as file:
        monkeys = []
        # Init
        for monkey_block in [block.split("\n")for block in file.read().split("\n\n")]:
            monkeys.append(Monkey(monkey_block))
        for _ in range(round_amount):
            # One round
            for monkey in monkeys:
                for item in monkey.starting_items:
                    monkey.inspection_count += 1
                    new_value = int(eval(str(item)+monkey.operation_str)) // 3
                    if new_value % monkey.divisor == 0:
                        monkeys[monkey.target1].starting_items.append(new_value)
                    else:
                        monkeys[monkey.target2].starting_items.append(new_value)
                monkey.starting_items = []
        sorted_monkeys = sorted(monkeys, key=lambda a: -a.inspection_count)
        return sorted_monkeys[0].inspection_count * sorted_monkeys[1].inspection_count

def part2(filename, round_amount = 20) -> int:
    with open(filename,"r") as file:
        monkeys = []
        least_common_multiple = 1
        # Init
        for monkey_block in [block.split("\n")for block in file.read().split("\n\n")]:
            new_monkey = Monkey(monkey_block)
            monkeys.append(new_monkey)
            least_common_multiple *= new_monkey.divisor
        for _ in range(round_amount):
            # One round
            for monkey in monkeys:
                for item in monkey.starting_items:
                    monkey.inspection_count += 1
                    new_value = eval(str(item)+monkey.operation_str) % least_common_multiple
                    if new_value % monkey.divisor == 0:
                        monkeys[monkey.target1].starting_items.append(new_value)
                    else:
                        monkeys[monkey.target2].starting_items.append(new_value)
                monkey.starting_items = []
        sorted_monkeys = sorted(monkeys, key=lambda a: -a.inspection_count)
        return sorted_monkeys[0].inspection_count * sorted_monkeys[1].inspection_count
            
if __name__ == "__main__":
    print("Part 1:",part1("11.in", 20))
    print("Part 2:", part2("11.in", 10000))