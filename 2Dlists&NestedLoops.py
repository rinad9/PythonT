from tkinter.tix import COLUMN


number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#     [row][column]
print(number_grid[0][0]) # 1

# nested for loop
for row in number_grid:
    print(row)

# to access each element we do Nested for loop
for row in number_grid:
    for col in row:
        print(col)