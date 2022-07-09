from pprint import pprint as pp
from numpy import asarray

# def solve_sodoku(puzzle):
# data = asarray(puzzle)
# # print(data)
# pp(data.size)
# # for row in data:
# #     row.set
# cols = zip(*data)
#
# for row in data:
#     needed_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for i in range(len(row)):
#         if row[i] != 0:
#             needed_nums.remove(row[i])
#         else:
#             row[i] = needed_nums
#
# pp(data)

#     for row in puzzle:
#         needed_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         for i in range(len(row)):
#             if row[i] != 0:
#                 needed_nums.remove(row[i])
#         for i in range(len(row)):
#             if row[i] == 0:
#                 row[i] = needed_nums
#     # pp(puzzle)
#     # print(len(puzzle)
#     print(columns)
#
#
# solve_sodoku([[5, 3, 0, 0, 7, 0, 0, 0, 0],
#               [6, 0, 0, 1, 9, 5, 0, 0, 0],
#               [0, 9, 8, 0, 0, 0, 0, 6, 0],
#               [8, 0, 0, 0, 6, 0, 0, 0, 3],
#               [4, 0, 0, 8, 0, 3, 0, 0, 1],
#               [7, 0, 0, 0, 2, 0, 0, 0, 6],
#               [0, 6, 0, 0, 0, 0, 2, 8, 0],
#               [0, 0, 0, 4, 1, 9, 0, 0, 5],
#               [0, 0, 0, 0, 8, 0, 0, 7, 9]])

# Giving up as it is taking too long (out of timebox)

"""
GIVEN SOLUTION
"""
from itertools import product  # product finds the cartesian product aka permuations of coordinates in this instance


def solve_sudoku(puzzle):
    for (row, col) in product(range(0, 9), repeat=2):
        if puzzle[row][col] == 0:  # find an unassigned cell
            for num in range(1, 10):
                allowed = True  # check if num is allowed in row/col/box
                for i in range(9):
                    if puzzle[i][col] == num or puzzle[row][i] == num:
                        allowed = False;
                        break  # not allowed in row or col
                for (i, j) in product(range(0, 3), repeat=2):
                    if puzzle[row - row % 3 + i][col - col % 3 + j] == num:
                        allowed = False;
                        break
                if allowed:
                    puzzle[row][col] = num
                    if trial := solve_sudoku(puzzle):
                        return trial
                    else:
                        puzzle[row][col] = 0
            return False
    return puzzle


print(solve_sudoku([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]]))

### REFLECTION ###
# The given algorithm is a backtracking algorithm employing DFS
# It uses an algorithm which not innate with human nature - I had been trying to implement a human-centric approach
# This algorithm used a trial and error approach.
# Learns whether it cannot be in a row, column or 3x3 grid and if it can places it
# It then recursively calls the sudoku function with the updated grid
# The solution given uses an assignment operator I have never come across in python before ':='
# This captures the return value on the same line if the function is able to continue
# If the function cannot continue and has to backtrack the else statement will reset the grid cell to 0
# That's the break keywords helping out
# Code also uses a repeat keyword this relates to the product module which is equivalent to a nested for loop
# This solution doesn't seem to be the most efficient with a time complexity of n^4 however it is function, which my
# function never got to be
