# Recogiendo fresas
# Count binary search iterations.

def binary_search_count(size, iterations):
    if size // 2 == 1:
        return iterations + 1
    else:
        iterations += 1
        return binary_search_count(size // 2, iterations)


def main():
    size = int(input())
    while size != - 1:
        print(binary_search_count(size, 1))
        size = int(input())


if __name__ == '__main__':
    main()
