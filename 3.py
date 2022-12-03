import string

# Teil 1
with open("3.in","r") as file:
    sum = 0
    for line in file.readlines():
        for char in line[:len(line) // 2]:
            if char in line[(len(line) // 2):]:
                sum += string.ascii_letters.index(char) + 1
                break
    print(sum)

# Teil 2
with open("3.in","r") as file:
    sum = 0
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        r1 = lines[i].strip()
        r2 = lines[i+1].strip()
        r3 = lines[i+2].strip()
        for char in r1:
            if char in r2 and char in r3:
                sum += string.ascii_letters.index(char) + 1
                break
    print(sum)
                    
