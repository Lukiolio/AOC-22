stacks = [
    ['R', 'C', 'H'],
    ['F', 'S', 'L', 'H', 'J', 'B'],
    ['Q', 'T', 'J', 'H', 'D', 'M', 'R'],
    ['J', 'B', 'Z', 'H', 'R', 'G', 'S'],
    ['B', 'C', 'D', 'T', 'Z', 'F', 'P', 'R'],
    ['G', 'C', 'H', 'T'],
    ['L', 'W', 'P', 'B', 'Z', 'V', 'N', 'S'],
    ['C', 'G', 'Q', 'J', 'R'],
    ['S', 'F', 'P', 'H', 'R', 'T', 'D', 'L']]

# Teil 1 & Teil 2 (für Teil 2 einfach 'elements_to_move.reverse()' auskommentieren)
with open("5.in") as file:
    for line in file.readlines():
        amount = int(line.split(" ")[1])
        start_stack_index = int(line.split(" ")[3]) - 1
        end_stack_index = int(line.split(" ")[5]) - 1
    
        elements_to_move = stacks[start_stack_index][:amount]
        elements_to_move.reverse()
        stacks[start_stack_index] = stacks[start_stack_index][amount:]
        stacks[end_stack_index] = elements_to_move + stacks[end_stack_index]
    total_string = "".join([stack[0] for stack in stacks])
    print(total_string)
