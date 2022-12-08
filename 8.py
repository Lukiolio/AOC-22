with open("8.in","r") as file:
    rows = [line.strip() for line in file.readlines()]
    forest_grid = []
    for row in rows:
        forest_grid.append([int(char) for char in row])

def get_visible_count():
    count_visible = 0
    for row in range(len(forest_grid)):
        for column in range(len(forest_grid[row])):
            if row not in range(1, len(forest_grid)-1) or column not in range(1, len(forest_grid[row])-1):
                # border
                count_visible += 1
            else:
                current_tree_height = forest_grid[row][column]
                left = True
                right = True
                up = True
                down = True
                for tree_height in forest_grid[row][:column]:
                    # left
                    if tree_height >= current_tree_height:
                        left = False
                        break
                for tree_height in forest_grid[row][column+1:]:
                    if tree_height >= current_tree_height:
                        right = False
                        break
                for i in range(row):
                    # up
                    if forest_grid[i][column] >= current_tree_height:
                        up = False
                        break
                for i in range(row+1,len(forest_grid)):
                    # down
                    if forest_grid[i][column] >= current_tree_height:
                        down = False
                        break
                if left or right or up or down:
                    count_visible += 1
    return count_visible
        
def get_top_scenic_score() -> int:
    top_scenic_score = 0
    for row in range(1, len(forest_grid) - 1):
        for column in range(1, len(forest_grid[row]) - 1):
            cur_height = forest_grid[row][column]
            cur_scenic_score = 1
            sum = 0
            # left
            for i in reversed(range(0, column)):
                sum +=1
                if forest_grid[row][i] >= cur_height:
                    break
            cur_scenic_score *= sum
            sum = 0
            # right
            for i in range(column+1, len(forest_grid[row])):
                sum +=1
                if forest_grid[row][i] >= cur_height:
                    break
            cur_scenic_score *= sum
            sum = 0
            # up
            for i in reversed(range(0, row)):
                sum +=1
                if forest_grid[i][column] >= cur_height:
                    break
            cur_scenic_score *= sum
            sum = 0
            # down
            for i in range(row+1, len(forest_grid)):
                sum +=1
                if forest_grid[i][column] >= cur_height:
                    break
            cur_scenic_score *= sum
            sum = 0
            top_scenic_score = cur_scenic_score if cur_scenic_score > top_scenic_score else top_scenic_score
    return top_scenic_score

if __name__ == "__main__":
    print("Part 1:",get_visible_count())
    print("Part 2:",get_top_scenic_score())