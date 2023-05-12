# Reina de Picas
# Count the best path steps in a maze, passing through required tiles, and banning others.

from math import inf

MOVEMENTS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_feasible(maze, i, j):
    if 0 <= i < len(maze) and 0 <= j < len(maze[0]):
        return maze[i][j] != 'w'


def maze_min_steps(maze, tile, end_tile, step, min_steps, rewards_gained, rewards_amount):
    if tile == end_tile and rewards_gained == rewards_amount:
        if step < min_steps:
            min_steps = step
    else:
        i, j = tile
        for i_movement, j_movement in MOVEMENTS:
            next_i = i + i_movement
            next_j = j + j_movement

            if is_feasible(maze, next_i, next_j):

                reward_picked = False
                if maze[next_i][next_j] == 'r':
                    rewards_gained += 1
                    reward_picked = True
                maze[next_i][next_j] = 'w'
                min_steps = maze_min_steps(maze, (next_i, next_j), end_tile, step + 1, min_steps, rewards_gained, rewards_amount)

                if reward_picked:
                    rewards_gained -= 1
                    maze[next_i][next_j] = 'r'
                else:
                    maze[next_i][next_j] = 'f'

    return min_steps


def main():
    rows_amount, columns_amount = map(int, input().strip().split())
    maze = [[] for _ in range(rows_amount)]
    for row in range(rows_amount):
        maze[row] = list(input().strip().split())

    # Change turret areas by walls:
    for i in range(rows_amount):
        for j in range(columns_amount):
            if maze[i][j] == 't':
                for wall_i in range(i - 1, i + 2):
                    for wall_j in range(j - 1, j + 2):
                        if 0 <= wall_i < rows_amount and 0 <= wall_j < columns_amount:
                            maze[wall_i][wall_j] = 'w'

    # Get remaining special tiles:
    start_tile = None
    end_tile = None
    rewards_amount = 0
    for i in range(rows_amount):
        for j in range(columns_amount):
            if maze[i][j] == 's':
                start_tile = (i, j)
                maze[i][j] = 'w'
            elif maze[i][j] == 'e':
                end_tile = (i, j)
            elif maze[i][j] == 'r':
                rewards_amount += 1

    rewards_gained = 0
    min_steps = inf
    step = 1

    print(maze_min_steps(maze, start_tile, end_tile, step, min_steps, rewards_gained, rewards_amount))


if __name__ == "__main__":
    main()
