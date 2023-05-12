# Casi sudoku
# Solve a sudoku or tell if it has none ore multiple solutions.
# Solved with a backtracking algorithm.

import copy


def print_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=' ')
        print()
    print()


def is_feasible(data, num, i, j):
    return not data['row'][i][num] and not data['column'][j][num] and not data['square'][i // 3][j // 3][num]


def solve_sudoku(data, tile):
    if tile == len(data['empty_tiles']):
        if data['solutions_amount'] == 0:
            data['first_solution'] = copy.deepcopy(data['sudoku'])
        data['solutions_amount'] += 1
    else:
        if data['solutions_amount'] < 2:
            i, j = data['empty_tiles'][tile]
            number = data['sudoku'][i][j]
            while number < 9:
                number += 1
                if is_feasible(data, number, i, j):
                    data['sudoku'][i][j] = number
                    data['row'][i][number] = True
                    data['column'][j][number] = True
                    data['square'][i // 3][j // 3][number] = True

                    data = solve_sudoku(data, tile + 1)

                    if data['solutions_amount'] < 2:
                        data['sudoku'][i][j] = 0
                        data['row'][i][number] = False
                        data['column'][j][number] = False
                        data['square'][i // 3][j // 3][number] = False
    return data


def main():
    data = {
        'solutions_amount': 0,
        'empty_tiles': [],
        'row': [[False] * 10 for _ in range(9)],
        'column': [[False] * 10 for _ in range(9)],
        'square': [[[False] * 10 for _ in range(3)] for _ in range(3)],
        'sudoku': [[] for _ in range(9)],
        'first_solution': None
    }

    for row in range(9):
        data['sudoku'][row] = list(map(int, input().strip().split()))

    for i in range(9):
        for j in range(9):
            number = data['sudoku'][i][j]
            if number != 0:
                data['row'][i][number] = True
                data['column'][j][number] = True
                data['square'][i // 3][j // 3][number] = True
            else:
                data['empty_tiles'].append((i, j))

    data = solve_sudoku(data, 0)

    if data['solutions_amount'] == 0:
        print('imposible')
    elif data['solutions_amount'] == 1:
        print_sudoku(data['first_solution'])
    else:
        print('casi sudoku')


if __name__ == "__main__":
    main()
