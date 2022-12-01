# Teil 1
with open("1.in", "r") as file:
    current_amount = 0
    highest_amount = 0
    for line in file.readlines():   
        if len(line.strip()) == 0:
            if(current_amount > highest_amount):
                highest_amount = current_amount
            current_amount = 0
        else:
            current_amount += int(line.strip())
    print(highest_amount)

# Teil 2
with open("1.in", "r") as file:
    top_3_amount = [0,0,0]
    current_amount = 0
    for line in file.readlines():   
        if len(line.strip()) == 0:
            top_3_amount.sort()
            for i in range(0,3):
                if current_amount > top_3_amount[i]:
                    top_3_amount[i] = current_amount
                    break
            current_amount = 0
        else:
            current_amount += int(line.strip())
    total_amount = 0
    for value in top_3_amount:
        total_amount += value
    print(total_amount)