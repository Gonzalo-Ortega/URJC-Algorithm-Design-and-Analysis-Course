# Binary search

def recursive_binary_search(v, number, low, high):
    # Base case:
    if low > high:
        return "Not found"
    middle = (low + high) // 2
    if v[middle] == number:
        return middle
    elif number < v[middle]:
        return recursive_binary_search(v, number, low, middle - 1)
    else:
        return recursive_binary_search(v, number, middle + 1, high)


def binary_search(v, number):
    return recursive_binary_search(v, number, 0, len(v) - 1)


def main():
    v = [1, 3, 3, 5, 6, 7, 9]
    number = 0
    print(binary_search(v, number))


if __name__ == "__main__":
    main()
