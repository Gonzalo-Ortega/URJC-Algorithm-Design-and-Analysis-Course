# Maze
# Find the shortest path to cross the maze, in case it exist.

import copy
from math import inf


def print_maze(maze):
    for row in range(len(maze)):
        for colum in range(len(maze[0])):
            if maze[row][colum] == inf:
                print("*", end="\t")
            elif maze[row][colum] == 0:
                print(" ", end="\t")
            else:
                print(maze[row][colum], end="\t")
        print()
    print()


def initialize_maze():
    rows_amount = 10
    columns_amount = 10

    maze = [[0 for _ in range(columns_amount)] for _ in range(rows_amount)]

    walls = [(0, 2), (0, 7), (1, 0), (1, 2), (1, 5), (1, 6), (1, 8), (2, 6), (2, 8), (3, 1), (3, 4), (3, 5), (3, 6),
             (4, 2), (4, 3), (4, 7), (5, 5), (5, 7), (6, 0), (6, 3), (6, 4), (6, 7), (6, 9), (7, 1), (7, 2), (7, 8),
             (7, 9), (8, 2), (8, 4), (8, 5)]  # Walls coordinates

    for row, colum in walls:
        maze[row][colum] = inf
    return maze


def is_solution(maze, row, colum):
    return row == len(maze) - 1 and colum == len(maze[0]) - 1


def is_better(solution_1, solution_2):
    row_amount = len(solution_1) - 1
    colum_amount = len(solution_1[0]) - 1
    return solution_1[row_amount][colum_amount] < solution_2[row_amount][colum_amount]


def is_feasible(maze, row, colum):
    if 0 <= row < len(maze) and 0 <= colum < len(maze[0]):
        return maze[row][colum] == 0
    else:
        return False


def backtracking_maze(maze, best_solution, row, colum, step):
    if is_solution(maze, row, colum):
        if is_better(maze, best_solution):
            best_solution = copy.deepcopy(maze)
    else:
        movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for row_movement, colum_movement in movements:
            new_row = row + row_movement
            new_colum = colum + colum_movement
            if is_feasible(maze, new_row, new_colum):
                maze[new_row][new_colum] = step
                best_solution = backtracking_maze(maze, best_solution, new_row, new_colum, step + 1)
                maze[new_row][new_colum] = 0

    return best_solution


def main():
    maze = initialize_maze()
    best_solution = copy.deepcopy(maze)
    best_solution[len(maze) - 1][len(maze) - 1] = inf

    row = 0
    colum = 0
    step = 1
    maze[row][colum] = step

    best_solution = backtracking_maze(maze, best_solution, row, colum, step + 1)
    print_maze(best_solution)


if __name__ == "__main__":
    main()
