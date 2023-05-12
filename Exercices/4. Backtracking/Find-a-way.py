# Find a way
# Maze but all empty tiles need to be covered and just need to determine if exists a solution.

MOVEMENTS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_feasible(maze, i, j, visited_tiles):
    if 0 <= i < len(maze) and 0 <= j < len(maze):
        return maze[i][j] != -1 and (i, j) not in visited_tiles


def fill_maze(maze, visited_tiles, tile, to_fill_tiles):
    if tile == (len(maze) - 1, len(maze) - 1) and len(visited_tiles) == to_fill_tiles:
        success = True
    else:
        success = False
        i, j = tile
        for i_movement, j_movement in MOVEMENTS:
            next_i = i + i_movement
            next_j = j + j_movement
            if is_feasible(maze, next_i, next_j, visited_tiles):
                visited_tiles.add((next_i, next_j))
                success = fill_maze(maze, visited_tiles, (next_i, next_j), to_fill_tiles)
                if not success:
                    visited_tiles.remove((next_i, next_j))
                else:
                    break
    return success


def main():
    maze_size = int(input().strip())
    maze = [[] for _ in range(maze_size)]
    for row in range(maze_size):
        maze[row] = list(map(int, input().strip().split()))

    to_fill_tiles = 0
    for i in range(maze_size):
        for j in range(maze_size):
            if maze[i][j] == 0:
                to_fill_tiles += 1

    initial_tile = (0, 0)
    visited_tiles = {initial_tile}

    print('SI' if fill_maze(maze, visited_tiles, initial_tile, to_fill_tiles) else 'NO')


if __name__ == "__main__":
    main()
