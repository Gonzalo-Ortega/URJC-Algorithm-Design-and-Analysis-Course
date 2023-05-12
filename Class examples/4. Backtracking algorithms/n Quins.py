# n Quins # INCOMPLETE
# Place n quins in a board avoiding them from threaten each other.

# There are three types of backtracking problems:
# To look for just one solution, for all solutions or for the best solution.
# In this case we are looking just for one.

def print_solution(solution):
    n = len(solution)
    board = [[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        board[row][solution[row]] = 1
        for colum in range(n):
            print(board[row][colum], end=' ')
        print()


def is_feasible(case, row, colum):
    feasible = True
    current_row = 1
    while feasible and current_row <= row:
        feasible_colum = case[row - current_row] != colum
        feasible_diagonal_1 = case[row - current_row] != colum - current_row
        feasible_diagonal_2 = case[row - current_row] != colum + current_row
        feasible = feasible_colum and feasible_diagonal_1 and feasible_diagonal_2
        current_row += 1
    return feasible


def is_solution(case, row):
    return row >= len(case)


def backtracking_n_quins(case, row):
    if is_solution(case, row):
        found_solution = True
    else:
        column = 0
        found_solution = False
        while not found_solution and column < len(case):
            if is_feasible(case, row, column):
                case[row] = column
                case, found_solution = backtracking_n_quins(case, row + 1)
                if not found_solution:
                    case[row] = -1
            column += 1
    return case, found_solution


def main():
    n = 8
    initial_case = [-1] * n  # Represents the position a quin is placed in each row.
    initial_row = 0  # Backtracking level.

    solution, success = backtracking_n_quins(initial_case, initial_row)

    print_solution(solution) if success else print("No solution")


if __name__ == "__main__":
    main()
