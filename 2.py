my_score_code = {"X":1,"Y":2,"Z":3}
opponent_score_code = {"A":1,"B":2,"C":3}

# Teil 1
result_matrix = [[4,8,3],[1,5,9],[7,2,6]]
game_results = []

with open("2.in","r") as file:
    for line in file.readlines():
        opponent_index = opponent_score_code[line.split(" ")[0].strip()]
        my_index = my_score_code[line.split(" ")[1].strip()]
        game_results.append(result_matrix[opponent_index - 1][my_index - 1])

total = 0
for result in game_results:
    total += result
print(total)

# Teil 2
result_matrix2 = [[3,4,8],[1,5,9],[2,6,7]]
game_results2 = []
with open("2.in","r") as file:
    for line in file.readlines():
        opponent_index = opponent_score_code[line.split(" ")[0].strip()]
        result_index = my_score_code[line.split(" ")[1].strip()]
        game_results2.append(result_matrix2[opponent_index - 1][result_index - 1])

total2 = 0
for result in game_results2:
    total2 += result
print(total2)