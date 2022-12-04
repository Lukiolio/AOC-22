# Teil 1
with open("4.in","r") as file:
    sum_fully_containing = 0
    for line in file.readlines():
        ranges1 = list(range(int(line.split(",")[0].split("-")[0]),int(line.split(",")[0].split("-")[1]) + 1))
        ranges2 = list(range(int(line.split(",")[1].split("-")[0]),int(line.split(",")[1].split("-")[1]) + 1))
        if set(ranges1).issubset(set(ranges2)) or set(ranges2).issubset(set(ranges1)):
            sum_fully_containing += 1
    print(sum_fully_containing)

# Teil 2
with open("4.in","r") as file:
    sum_fully_containing = 0
    for line in file.readlines():
        ranges1 = list(range(int(line.split(",")[0].split("-")[0]),int(line.split(",")[0].split("-")[1]) + 1))
        ranges2 = list(range(int(line.split(",")[1].split("-")[0]),int(line.split(",")[1].split("-")[1]) + 1))
        if len(set(ranges1) & set(ranges2)) > 0:
            sum_fully_containing += 1
        
    print(sum_fully_containing)