# Horse Luis
# Shortest length path in a maze with order requirement tiles.

MOVEMENTS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_feasible(room, tile, row_movement, colum_movement, last_tile_content, visited_tiles):
    new_row = tile[0] + row_movement
    new_colum = tile[1] + colum_movement
    return 0 <= new_row < len(room) and 0 <= new_colum < len(room[0]) and \
        (new_row, new_colum) not in visited_tiles and \
        (room[new_row][new_colum] == last_tile_content + 1 or room[new_row][new_colum] == 0)


def path_tiles_amount(room, tile, last_tile_content, visited_tiles, pieces_amount, min_steps):
    if last_tile_content == pieces_amount:
        min_steps = min(min_steps, len(visited_tiles))
    else:
        for row_movement, colum_movement in MOVEMENTS:
            tile_type_update = False
            if is_feasible(room, tile, row_movement, colum_movement, last_tile_content, visited_tiles):
                new_row = tile[0] + row_movement
                new_colum = tile[1] + colum_movement
                visited_tiles.add((new_row, new_colum))
                if room[new_row][new_colum] == last_tile_content + 1:
                    last_tile_content += 1
                    tile_type_update = True
                min_steps = min(min_steps, path_tiles_amount(room, (new_row, new_colum), last_tile_content, visited_tiles, pieces_amount, min_steps))
                if tile_type_update:
                    last_tile_content -= 1
                visited_tiles.remove((new_row, new_colum))
    return min_steps


def main():
    row_amount, colum_amount, pieces_amount = map(int, input().strip().split())
    room = []
    for _ in range(row_amount):
        row = list(map(int, input().strip().split()))
        room.append(row)
    start_tile = (0, 0)
    last_tile_content = 0
    visited_tiles = {start_tile}
    min_steps = 0x3f3f3f

    print(path_tiles_amount(room, start_tile, last_tile_content, visited_tiles, pieces_amount, min_steps))


if __name__ == "__main__":
    main()
