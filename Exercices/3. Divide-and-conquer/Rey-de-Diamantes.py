# Rey de corazones
# Binary search getting the equal or upper of search number and deleting items over iterations.

def binary_approx_search(data, number, low, high):
    if low > high:
        return low
    middle = (low + high) // 2
    if data[middle] == number:
        return middle
    elif number < data[middle]:
        return binary_approx_search(data, number, low, middle - 1)
    else:
        return binary_approx_search(data, number, middle + 1, high)


def main():
    grid_size = int(input().strip())
    data = []
    for _ in range(grid_size):
        data.extend(list(map(int, input().strip().split())))

    iterations = list(map(int, input().strip().split()))
    removed_indexes = set()

    for number in iterations:
        index = binary_approx_search(data, number, 0, len(data) - 1)
        while index in removed_indexes and index < len(data) - 1:
            index += 1
        removed_indexes.add(index)

    for index in range(len(data)):
        print("X" if index in removed_indexes else data[index], end=" ")
        if index % grid_size == grid_size - 1:
            print()


if __name__ == "__main__":
    main()
