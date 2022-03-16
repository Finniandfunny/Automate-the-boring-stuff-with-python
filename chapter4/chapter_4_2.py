#Topic : List


grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

for r in range(len(grid[0])):  #checks how many are there in first element
    for l in range(len(grid)): #checks how many are there in grid
        print(grid[l][r],end="") #gives the column
        # "end" is to avoid newline
    print() #breaks line and gives the row